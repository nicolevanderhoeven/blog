#!/usr/bin/env python3
"""Find Nicole's new videos and blog posts and write them as Hugo posts.

Sources (all public, no API keys):
  * grafana/developer-advocacy ``transcripts/`` (every video on the Grafana
    YouTube channel); a video counts as Nicole's when her name appears in its
    title, description or summary.
  * Nicole's own YouTube channel, through its public RSS feed.
  * Blog feeds listed in ``config.json`` (RSS or Atom).

Everything already on the site (matched by YouTube video id or URL), anything
older than the start date and anything private or not yet public is skipped.
Posts are generated only from facts in the source (title, date, description or
summary): no text is written by a model.

Usage (from the repository root):

    python3 scripts/auto_posts/auto_posts.py --dev-advocacy-dir PATH [--dry-run]

See README.md ("Automatic posts") for details.
"""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import html
import json
import re
import sys
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable, Optional

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CONFIG_PATH = HERE / "config.json"
USER_AGENT = "nicolevanderhoeven.com-auto-posts (+https://github.com/nicolevanderhoeven/site-nicolevdh)"

HOME_PAGES = ("layouts/index.html", "themes/cactus/layouts/index.html")


# --------------------------------------------------------------------------
# Data model
# --------------------------------------------------------------------------

@dataclass
class Item:
    """One video or blog post found in a source."""

    kind: str  # "video" or "blog"
    url: str
    title: str
    published: dt.datetime  # timezone aware
    description: str = ""
    source: str = ""  # human label, e.g. "Context Horizon"
    video_id: str = ""
    source_tags: list = field(default_factory=list)
    match_text: str = ""  # extra text (summary, topics) used for tagging only


@dataclass
class SiteIndex:
    video_ids: set
    urls: set
    tags: dict  # tag -> number of posts using it
    newest_video: Optional[dt.datetime]


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

_YT_PATTERNS = [
    re.compile(r"\{\{<\s*youtube\s+(?:id=)?[\"']?([A-Za-z0-9_-]{11})[\"']?\s*>\}\}"),
    re.compile(
        r"(?:youtube(?:-nocookie)?\.com/(?:watch\?(?:[^\"\s)#]*&)?v=|embed/|shorts/|live/)"
        r"|youtu\.be/)([A-Za-z0-9_-]{11})"
    ),
]


def youtube_ids(text: str) -> set:
    """Every YouTube video id referenced in ``text`` (shortcode, iframe or link)."""
    found = set()
    for pattern in _YT_PATTERNS:
        found.update(pattern.findall(text))
    return found


def normalize_url(url: str) -> str:
    """Comparable form of a URL: no scheme, ``www.``, query, fragment or trailing slash."""
    url = html.unescape(url.strip())
    url = re.sub(r"^[a-z]+://", "", url, flags=re.I)
    ids = youtube_ids("https://" + url)
    if ids:  # any YouTube link form (watch, embed, youtu.be) is just its video id
        return "youtube:" + sorted(ids)[0]
    url = url.split("#", 1)[0].split("?", 1)[0]
    url = re.sub(r"^www\.", "", url, flags=re.I)
    return url.rstrip("/").lower()


_URL_RE = re.compile(r"https?://[^\s)\"'<>\]]+")


def parse_datetime(value: str) -> Optional[dt.datetime]:
    """Parse an ISO 8601 or RFC 2822 timestamp into an aware UTC datetime."""
    value = (value or "").strip()
    if not value:
        return None
    parsed = None
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        try:
            parsed = email.utils.parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        if tag in ("p", "br", "div", "li", "h1", "h2", "h3", "h4"):
            self.parts.append("\n\n")


def html_to_text(value: str) -> str:
    """Plain text of an HTML snippet, paragraphs separated by a blank line."""
    parser = _TextExtractor()
    parser.feed(value or "")
    text = "".join(parser.parts).replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s*\n\s*\n\s*", "\n\n", text)
    return text.strip()


def excerpt(text: str, limit: int = 400) -> str:
    """First paragraph(s) of ``text`` cut at a word boundary after ``limit`` characters."""
    text = text.strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(",;:-")
    return cut + "…"


def slugify(title: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rsplit("-", 1)[0] or text[:max_len]
    return text or "post"


def load_config(path: Path = CONFIG_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def name_regex(config: dict) -> re.Pattern:
    return re.compile("|".join("(?:%s)" % p for p in config["name_patterns"]), re.I)


# --------------------------------------------------------------------------
# What is already on the site
# --------------------------------------------------------------------------

_FRONT_DATE = re.compile(r"^date:\s*[\"']?([^\"'\n]+?)[\"']?\s*$", re.M)
_FRONT_TAGS = re.compile(r"^tags:\s*\[(.*)\]\s*$", re.M)


def scan_site(content_dir: Path) -> SiteIndex:
    """Collect the video ids, URLs and tags used by existing posts."""
    video_ids: set = set()
    urls: set = set()
    tags: dict = {}
    newest: Optional[dt.datetime] = None
    for path in sorted(Path(content_dir).rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        ids = youtube_ids(text)
        video_ids |= ids
        urls.update(normalize_url(u) for u in _URL_RE.findall(text))
        match = _FRONT_TAGS.search(text)
        if match:
            for tag in {t.lower() for t in re.findall(r"[\"']([^\"']+)[\"']", match.group(1))}:
                tags[tag] = tags.get(tag, 0) + 1
        date = _FRONT_DATE.search(text)
        if ids and date:
            when = parse_datetime(date.group(1))
            if when and (newest is None or when > newest):
                newest = when
    return SiteIndex(video_ids, urls, tags, newest)


# --------------------------------------------------------------------------
# Source: grafana/developer-advocacy transcripts
# --------------------------------------------------------------------------

_SKIP_TITLES = re.compile(r"^(private video|deleted video)$", re.I)


def _section(text: str, heading: str) -> str:
    match = re.search(r"^## %s\s*\n(.*?)(?=^## |\Z)" % re.escape(heading), text, re.M | re.S)
    return match.group(1).strip() if match else ""


def parse_transcript(text: str) -> Optional[Item]:
    """Parse one developer-advocacy transcript file into a video ``Item``.

    Only the title, description, summary and topics are used: never the
    transcript itself, which mentions many people called Nicole.
    """
    title_match = re.match(r"#\s+(.+)", text)
    published = re.search(r"^Published on (\S+)", text, re.M)
    if not title_match or not published:
        return None
    title = html.unescape(title_match.group(1).strip())
    when = parse_datetime(published.group(1))
    if not when or _SKIP_TITLES.match(title):
        return None
    description_block = _section(text, "Description")
    url_match = re.search(r"^URL:\s*(\S+)", description_block, re.M)
    if not url_match:
        return None
    ids = youtube_ids(url_match.group(1))
    if not ids:
        return None
    description = html.unescape(re.sub(r"^URL:.*$", "", description_block, flags=re.M).strip())
    summary = html.unescape(_section(text, "Summary"))
    return Item(
        kind="video",
        url="https://www.youtube.com/watch?v=%s" % next(iter(ids)),
        title=title,
        published=when,
        description=description,
        video_id=next(iter(ids)),
        match_text=summary,
    )


def load_developer_advocacy(directory: Path, config: dict, now: dt.datetime) -> list:
    """Nicole's videos among the developer-advocacy transcripts."""
    names = name_regex(config)
    section = config["developer_advocacy"]
    items = []
    for path in sorted(Path(directory).glob("*.md")):
        if not path.name[:1].isdigit():
            continue  # README.md, recurring-shows.md, ...
        item = parse_transcript(path.read_text(encoding="utf-8", errors="replace"))
        if not item or item.published > now:
            continue
        haystack = "\n".join([item.title, item.description, item.match_text])
        if not names.search(haystack):
            continue
        item.source = section["label"]
        item.source_tags = list(section["tags"])
        items.append(item)
    return items


# --------------------------------------------------------------------------
# Sources: YouTube channel RSS and blog feeds
# --------------------------------------------------------------------------

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "content": "http://purl.org/rss/1.0/modules/content/",
}


def _text(node: Optional[ET.Element]) -> str:
    return (node.text or "").strip() if node is not None else ""


def parse_youtube_feed(xml_text: str, config: dict, now: dt.datetime) -> list:
    """Public videos from a YouTube channel RSS feed."""
    root = ET.fromstring(xml_text)
    section = config["own_channel"]
    items = []
    for entry in root.findall("atom:entry", NS):
        video_id = _text(entry.find("yt:videoId", NS))
        when = parse_datetime(_text(entry.find("atom:published", NS)))
        title = _text(entry.find("atom:title", NS))
        if not video_id or not when or when > now or _SKIP_TITLES.match(title):
            continue
        description = _text(entry.find("media:group/media:description", NS))
        items.append(
            Item(
                kind="video",
                url="https://www.youtube.com/watch?v=%s" % video_id,
                title=title,
                published=when,
                description=clean_video_description(description),
                source=section["label"],
                video_id=video_id,
                source_tags=list(section["tags"]),
            )
        )
    return items


def clean_video_description(text: str, limit: int = 1200) -> str:
    """Keep the prose at the top of a YouTube description.

    Stops at the first chapter list, separator line or hashtag line, because
    those are not part of a post's introduction.
    """
    kept = []
    for line in text.replace("\r\n", "\n").split("\n"):
        stripped = line.strip()
        if re.match(r"^(\d{1,2}:)?\d{1,2}:\d{2}\b", stripped) or re.match(r"^[-=_*]{3,}$", stripped):
            break
        if stripped and all(word.startswith("#") for word in stripped.split()):
            break
        kept.append(line)
    cleaned = re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip()
    cleaned = cleaned.replace("{{", "{ {")  # never let a Hugo shortcode through
    return excerpt(cleaned, limit)


def parse_blog_feed(xml_text: str, feed: dict, names: re.Pattern, now: dt.datetime) -> list:
    """Posts from an RSS 2.0 or Atom feed, optionally only those written by Nicole."""
    root = ET.fromstring(xml_text)
    entries = []
    for node in root.iter():
        tag = node.tag.split("}")[-1]
        if tag in ("item", "entry"):
            entries.append((tag, node))
    items = []
    for tag, node in entries:
        if tag == "item":
            title = _text(node.find("title"))
            link = _text(node.find("link"))
            when = parse_datetime(_text(node.find("pubDate")) or _text(node.find("dc:date", NS)))
            author = _text(node.find("dc:creator", NS)) or _text(node.find("author"))
            summary = _text(node.find("description")) or _text(node.find("content:encoded", NS))
        else:
            title = _text(node.find("atom:title", NS))
            link_node = None
            for candidate in node.findall("atom:link", NS):
                if candidate.get("rel", "alternate") == "alternate":
                    link_node = candidate
                    break
            link = link_node.get("href", "") if link_node is not None else ""
            when = parse_datetime(_text(node.find("atom:published", NS)) or _text(node.find("atom:updated", NS)))
            author = _text(node.find("atom:author/atom:name", NS))
            summary = _text(node.find("atom:summary", NS)) or _text(node.find("atom:content", NS))
        if not title or not link or not when or when > now:
            continue
        if feed.get("filter_author") and not names.search(author):
            continue
        items.append(
            Item(
                kind="blog",
                url=link,
                title=html.unescape(title),
                published=when,
                description=excerpt(html_to_text(summary)),
                source=feed["label"],
                source_tags=list(feed.get("tags", [])),
            )
        )
    return items


def fetch(url: str, timeout: int = 30) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


# --------------------------------------------------------------------------
# Selecting what is new
# --------------------------------------------------------------------------

def start_of_day(when: dt.datetime) -> dt.datetime:
    return when.astimezone(dt.timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)


def select_new(items: Iterable[Item], site: SiteIndex, since: Optional[dt.datetime]) -> list:
    """Items not yet on the site and not older than ``since`` (by day), newest first.

    Duplicates between sources (same video id or URL) are collapsed, keeping
    the first one given.
    """
    cutoff = start_of_day(since) if since else None
    seen_ids: set = set()
    seen_urls: set = set()
    kept = []
    for item in items:
        key_url = normalize_url(item.url)
        if cutoff and item.published < cutoff:
            continue
        if item.video_id and (item.video_id in site.video_ids or item.video_id in seen_ids):
            continue
        if key_url in site.urls or key_url in seen_urls:
            continue
        if item.video_id:
            seen_ids.add(item.video_id)
        seen_urls.add(key_url)
        kept.append(item)
    return sorted(kept, key=lambda i: i.published, reverse=True)


# --------------------------------------------------------------------------
# Generating posts
# --------------------------------------------------------------------------

def _first_positions(text: str, candidates: Iterable[str]) -> list:
    """Candidates found in ``text`` as whole words, in order of first appearance."""
    lowered = text.lower()
    found = []
    for tag in candidates:
        match = re.search(r"(?<![\w-])%s(?![\w-])" % re.escape(tag), lowered)
        if match:
            found.append((match.start(), tag))
    return [tag for _, tag in sorted(found)]


def tags_for(item: Item, site_tags: dict, config: dict) -> list:
    """Tags for a post: facts-based, using only tags the site already uses."""
    tags: list = []

    def add(values):
        for value in values:
            if value not in tags:
                tags.append(value)

    text = "\n".join([item.title, item.description, item.match_text])
    generic = set(config["generic_tags"])
    vocabulary = sorted(
        t for t, uses in site_tags.items() if t not in generic and len(t) >= 2 and uses >= config["min_tag_uses"]
    )
    own = {t.lower() for t in item.source_tags}
    topic_tags = [t for t in _first_positions(text, vocabulary) if t not in own]
    add(topic_tags[: config["max_topic_tags"]])
    add(["english"])
    add(["video"] if item.kind == "video" else [])
    add(item.source_tags)
    for show in config["shows"]:
        if item.kind == "video" and re.search(show["pattern"], text, re.I):
            add(show["tags"])
    return tags


def front_matter(item: Item, tags: list) -> str:
    return "\n".join(
        [
            "---",
            "title: %s" % json.dumps(item.title, ensure_ascii=False),
            "date: %s" % item.published.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            "draft: false",
            "tags: [%s]" % ", ".join(json.dumps(t, ensure_ascii=False) for t in tags),
            "---",
        ]
    )


def render_post(item: Item, site_tags: dict, config: dict) -> str:
    """Markdown for one post, in the format of the existing video and link posts."""
    tags = tags_for(item, site_tags, config)
    parts = [front_matter(item, tags), ""]
    if item.kind == "video":
        if item.description:
            parts += [item.description.strip(), ""]
        parts += ["{{< youtube %s >}}" % item.video_id, ""]
    else:
        parts += ["Originally posted [here](%s) on %s." % (item.url, item.source), ""]
        if item.description:
            parts += [item.description.strip(), ""]
    return "\n".join(parts)


def filename_for(item: Item, taken: set) -> str:
    base = "%s-%s" % (item.published.strftime("%Y%m%d"), slugify(item.title))
    name, n = base + ".md", 2
    while name in taken:
        name = "%s-%d.md" % (base, n)
        n += 1
    taken.add(name)
    return name


def pr_title(items: list) -> str:
    videos = sum(1 for i in items if i.kind == "video")
    blogs = len(items) - videos
    pieces = []
    if videos:
        pieces.append("%d video%s" % (videos, "" if videos == 1 else "s"))
    if blogs:
        pieces.append("%d blog post%s" % (blogs, "" if blogs == 1 else "s"))
    return "New: " + ", ".join(pieces)


def pr_body(items: list, files: dict, config: dict, since: Optional[dt.datetime], home_video: Optional[Item]) -> str:
    lines = [
        "Automatically generated by `scripts/auto_posts/auto_posts.py` "
        "(scheduled workflow `Auto posts`). Review, edit and merge when ready; nothing is published until you merge.",
        "",
        "## New items",
        "",
    ]
    for item in items:
        lines.append(
            "- **%s**: [%s](%s) (%s, %s) → `content/blog/%s`"
            % (
                "Video" if item.kind == "video" else "Blog post",
                item.title.replace("[", "\\[").replace("]", "\\]"),
                item.url,
                item.source,
                item.published.strftime("%Y-%m-%d"),
                files[id(item)],
            )
        )
    if home_video:
        lines += ["", "## Home page", "", "Last Video embed now points to [%s](%s)." % (home_video.title, home_video.url)]
    lines += [
        "",
        "## Sources checked",
        "",
        "- Videos on the Grafana channel: [grafana/developer-advocacy](https://github.com/grafana/developer-advocacy/tree/main/transcripts) "
        "transcripts, matching Nicole by name in the title, description or summary",
        "- Videos on Nicole's own channel: https://www.youtube.com/feeds/videos.xml?channel_id=%s" % config["own_channel"]["id"],
    ]
    for feed in config["blog_feeds"]:
        suffix = " (only posts by Nicole)" if feed.get("filter_author") else ""
        lines.append("- Blog feed, %s: %s%s" % (feed["label"], feed["url"], suffix))
    if since:
        lines += ["", "Only items published on or after %s were considered." % since.strftime("%Y-%m-%d")]
    lines += [
        "",
        "Post text comes straight from the source (title, date, description or summary); tags are picked from tags already used on the site.",
        "",
    ]
    return "\n".join(lines)


def update_home_page(repo: Path, video_id: str) -> list:
    """Point the Last Video embed at ``video_id``; returns the files changed."""
    changed = []
    pattern = re.compile(
        r'(<section id="videos">.*?youtube\.com/embed/)([A-Za-z0-9_-]{11})',
        re.S,
    )
    for relative in HOME_PAGES:
        path = repo / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new_text, count = pattern.subn(lambda m: m.group(1) + video_id, text, count=1)
        if count and new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed.append(relative)
    return changed


# --------------------------------------------------------------------------
# Command line
# --------------------------------------------------------------------------

def gather(args, config: dict, now: dt.datetime) -> list:
    names = name_regex(config)
    items: list = []
    if args.dev_advocacy_dir:
        items += load_developer_advocacy(Path(args.dev_advocacy_dir), config, now)
    else:
        print("note: --dev-advocacy-dir not given, skipping Grafana channel videos", file=sys.stderr)
    sources = [("YouTube channel", lambda: parse_youtube_feed(
        fetch("https://www.youtube.com/feeds/videos.xml?channel_id=%s" % config["own_channel"]["id"]), config, now))]
    for feed in config["blog_feeds"]:
        sources.append((feed["label"], lambda feed=feed: parse_blog_feed(fetch(feed["url"]), feed, names, now)))
    failed = 0
    for label, load in sources:
        try:
            items += load()
        except Exception as error:  # one broken feed must not hide the others
            failed += 1
            print("::warning::could not read %s: %s" % (label, error), file=sys.stderr)
    if failed == len(sources):
        raise SystemExit("error: every online source failed, refusing to report 'nothing new'")
    return items


def main(argv: Optional[list] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dev-advocacy-dir", help="path to grafana/developer-advocacy's transcripts/ folder")
    parser.add_argument("--since", help="earliest publish date (YYYY-MM-DD); default: date of the newest existing video post")
    parser.add_argument("--repo", default=str(REPO), help="site repository root (default: this repository)")
    parser.add_argument("--output-dir", help="write pr-title.txt, pr-body.md and count.txt here (for the workflow)")
    parser.add_argument("--dry-run", action="store_true", help="print what would be created without writing files")
    args = parser.parse_args(argv)

    repo = Path(args.repo)
    config = load_config()
    now = dt.datetime.now(dt.timezone.utc)
    site = scan_site(repo / "content")
    since = parse_datetime(args.since) if args.since else site.newest_video
    print("start date: %s" % (since.strftime("%Y-%m-%d") if since else "none"), file=sys.stderr)

    new_items = select_new(gather(args, config, now), site, since)
    if args.output_dir:
        Path(args.output_dir).mkdir(parents=True, exist_ok=True)
        (Path(args.output_dir) / "count.txt").write_text(str(len(new_items)))
    if not new_items:
        print("nothing new")
        return 0

    taken = {p.name for p in (repo / "content" / "blog").glob("*.md")}
    files = {}
    for item in new_items:
        name = filename_for(item, taken)
        files[id(item)] = name
        body = render_post(item, site.tags, config)
        print("%s %s: %s" % ("would create" if args.dry_run else "creating", name, item.title))
        if not args.dry_run:
            (repo / "content" / "blog" / name).write_text(body, encoding="utf-8")

    newest_video = next((i for i in new_items if i.kind == "video"), None)
    home_ok = newest_video and (site.newest_video is None or newest_video.published >= site.newest_video)
    if not home_ok:
        newest_video = None
    if newest_video and not args.dry_run:
        for relative in update_home_page(repo, newest_video.video_id):
            print("updated %s" % relative)
    if args.output_dir:
        out = Path(args.output_dir)
        (out / "pr-title.txt").write_text(pr_title(new_items))
        (out / "pr-body.md").write_text(pr_body(new_items, files, config, since, newest_video))
    return 0


if __name__ == "__main__":
    sys.exit(main())
