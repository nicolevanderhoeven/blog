import datetime as dt
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import auto_posts as ap  # noqa: E402

CONFIG = ap.load_config()
NOW = dt.datetime(2026, 11, 21, 12, 0, tzinfo=dt.timezone.utc)
NAMES = ap.name_regex(CONFIG)

TRANSCRIPT = """# Build apps on your data with Grafana Pages (The Context Window #07)

Published on 2026-11-05T04:44:12Z

## Description

In Build apps on your data with Grafana Pages, episode 7 of The Context Window, we talk about ...

URL: https://www.youtube.com/watch?v=TjzXIMfLSTg

## Summary

Hosts Nicole VanderHoeven, Tiffany and Tom discussed Grafana Pages and AI.

Topics: Grafana Pages, observability.

## Chapters

00:00:00 Introduction

Nicole Smith said this only in the transcript.
"""

YOUTUBE_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns:yt="http://www.youtube.com/xml/schemas/2015" xmlns:media="http://search.yahoo.com/mrss/" xmlns="http://www.w3.org/2005/Atom">
 <entry><yt:videoId>AAAAAAAAAAA</yt:videoId><title>My own video</title><published>2026-11-10T10:00:00+00:00</published>
  <media:group><media:description>Short intro line.

00:00 Intro
01:00 Next</media:description></media:group></entry>
 <entry><yt:videoId>BBBBBBBBBBB</yt:videoId><title>Future video</title><published>2027-01-01T10:00:00+00:00</published></entry>
</feed>"""

RSS_FEED = """<?xml version="1.0"?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/"><channel>
 <item><title>Mine</title><link>https://example.com/p/mine?utm=1</link><pubDate>Thu, 12 Nov 2026 09:00:00 GMT</pubDate>
  <dc:creator>Nicole van der Hoeven</dc:creator><description>&lt;p&gt;First &amp;amp; foremost.&lt;/p&gt;&lt;p&gt;Second.&lt;/p&gt;</description></item>
 <item><title>Not mine</title><link>https://example.com/p/other</link><pubDate>Thu, 12 Nov 2026 09:00:00 GMT</pubDate>
  <dc:creator>Someone Else</dc:creator><description>x</description></item>
</channel></rss>"""

ATOM_FEED = """<?xml version="1.0"?>
<feed xmlns="http://www.w3.org/2005/Atom">
 <entry><title>Atom post</title><link rel="alternate" href="https://example.org/a"/><published>2026-11-11T08:00:00Z</published>
  <author><name>Nicole Vanderhoeven</name></author><summary>Atom summary.</summary></entry>
</feed>"""


def video(video_id="CCCCCCCCCCC", title="A video", published=dt.datetime(2026, 11, 8, tzinfo=dt.timezone.utc), **kw):
    return ap.Item(kind="video", url="https://www.youtube.com/watch?v=" + video_id, title=title,
                   published=published, video_id=video_id, source="Grafana YouTube channel", **kw)


def site(video_ids=(), urls=(), tags=None, newest=None):
    return ap.SiteIndex(set(video_ids), set(urls), tags or {}, newest)


class NameMatching(unittest.TestCase):
    def test_spelling_and_spacing_variants(self):
        for text in ["Nicole van der Hoeven", "NICOLE VAN DER HOEVEN", "Nicole Vanderhoeven", "Nicole VanderHoeven",
                     "Nicole  van  der  Hoeven", "Nicole Vanderhovven", "Nicole van-der-Hoeven", "Nicole van de Hoeven",
                     "ping nicolevdh", "@nicolevanderhoeven", "Nicole from Grafana", "Nicole from ..."]:
            self.assertTrue(NAMES.search(text), text)

    def test_other_people_called_nicole(self):
        for text in ["Nicole Smith", "Nicole said hello", "Nicole from Acme", "a vanderhoeven"]:
            self.assertFalse(NAMES.search(text), text)


class TranscriptParsing(unittest.TestCase):
    def test_fields(self):
        item = ap.parse_transcript(TRANSCRIPT)
        self.assertEqual(item.video_id, "TjzXIMfLSTg")
        self.assertEqual(item.published, dt.datetime(2026, 11, 5, 4, 44, 12, tzinfo=dt.timezone.utc))
        self.assertTrue(item.description.startswith("In Build apps"))
        self.assertNotIn("URL:", item.description)
        self.assertIn("Nicole VanderHoeven", item.match_text)
        self.assertNotIn("Nicole Smith", item.match_text)  # transcript text is never searched

    def test_html_entities_unescaped(self):
        item = ap.parse_transcript(TRANSCRIPT.replace("Build apps", "Don&#39;t build apps", 1))
        self.assertIn("Don't build apps", item.title)

    def test_private_or_incomplete_files_skipped(self):
        self.assertIsNone(ap.parse_transcript(TRANSCRIPT.replace("# Build apps on your data with Grafana Pages (The Context Window #07)", "# Private video", 1)))
        self.assertIsNone(ap.parse_transcript(TRANSCRIPT.replace("URL: https://www.youtube.com/watch?v=TjzXIMfLSTg", "")))
        self.assertIsNone(ap.parse_transcript("no heading"))

    def test_loader_matches_by_name_and_ignores_transcript_and_future(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            (tmp / "2026-11-05T04:44:12Z-hers.md").write_text(TRANSCRIPT)
            other = TRANSCRIPT.replace("Nicole VanderHoeven", "Someone").replace("TjzXIMfLSTg", "ZZZZZZZZZZZ")
            (tmp / "2026-11-06T00:00:00Z-other.md").write_text(other)
            future = TRANSCRIPT.replace("2026-11-05", "2027-01-05").replace("TjzXIMfLSTg", "YYYYYYYYYYY")
            (tmp / "2027-01-05T00:00:00Z-future.md").write_text(future)
            (tmp / "README.md").write_text(TRANSCRIPT.replace("ZZZ", "WWW"))
            found = ap.load_developer_advocacy(tmp, CONFIG, NOW)
        self.assertEqual([i.video_id for i in found], ["TjzXIMfLSTg"])
        self.assertEqual(found[0].source_tags, ["grafana labs"])


class Feeds(unittest.TestCase):
    def test_youtube_feed_skips_future_and_cuts_chapters(self):
        items = ap.parse_youtube_feed(YOUTUBE_FEED, CONFIG, NOW)
        self.assertEqual([i.video_id for i in items], ["AAAAAAAAAAA"])
        self.assertEqual(items[0].description, "Short intro line.")

    def test_rss_filters_author_and_cleans_html(self):
        feed = {"label": "Blog", "filter_author": True, "tags": ["x"]}
        items = ap.parse_blog_feed(RSS_FEED, feed, NAMES, NOW)
        self.assertEqual([i.title for i in items], ["Mine"])
        self.assertEqual(items[0].description, "First & foremost.\n\nSecond.")
        self.assertEqual(items[0].source_tags, ["x"])
        everyone = ap.parse_blog_feed(RSS_FEED, dict(feed, filter_author=False), NAMES, NOW)
        self.assertEqual(len(everyone), 2)

    def test_configured_feeds_filter_by_author_where_the_feed_has_many_authors(self):
        medium = ('<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/"><channel>'
                  '<item><title>Hers</title><link>https://medium.com/grafana-labs/hers-1?source=rss</link><pubDate>Fri, 13 Nov 2026 15:52:27 GMT</pubDate><dc:creator>Nicole van der Hoeven</dc:creator></item>'
                  '<item><title>Not hers</title><link>https://medium.com/grafana-labs/other-2</link><pubDate>Fri, 13 Nov 2026 15:52:27 GMT</pubDate><dc:creator>Marie Cruz</dc:creator></item>'
                  '</channel></rss>')
        feeds = {f["label"]: f for f in CONFIG["blog_feeds"]}
        unprompted = feeds["Grafana Labs Unprompted"]
        self.assertEqual(unprompted["url"], "https://medium.com/feed/grafana-labs")
        self.assertTrue(unprompted["filter_author"])
        self.assertNotIn("Medium", feeds)
        self.assertEqual([i.title for i in ap.parse_blog_feed(medium, unprompted, NAMES, NOW)], ["Hers"])

    def test_atom(self):
        items = ap.parse_blog_feed(ATOM_FEED, {"label": "A", "filter_author": True}, NAMES, NOW)
        self.assertEqual(items[0].url, "https://example.org/a")
        self.assertEqual(items[0].published.day, 11)


class DeDuplication(unittest.TestCase):
    def test_scan_site_finds_ids_urls_and_newest_video(self):
        with tempfile.TemporaryDirectory() as tmp:
            blog = Path(tmp) / "blog"
            blog.mkdir()
            (blog / "a.md").write_text('---\ndate: 2026-10-01T09:00:00+01:00\ntags: ["ai", "video"]\n---\n{{< youtube AAAAAAAAAAA >}}\n')
            (blog / "b.md").write_text('---\ndate: 2026-11-01T09:00:00+00:00\ntags: ["ai"]\n---\nsee https://youtu.be/BBBBBBBBBBB and [x](https://www.example.com/p/one/?utm=1)\n')
            (blog / "c.md").write_text('---\ndate: 2026-12-01T09:00:00+00:00\ntags: ["ai"]\n---\nNo video here.\n')
            (blog / "d.md").write_text('---\ndate: 2026-09-01T09:00:00+00:00\n---\n<iframe src="https://www.youtube.com/embed/DDDDDDDDDDD"></iframe>\n')
            index = ap.scan_site(Path(tmp))
        self.assertEqual(index.video_ids, {"AAAAAAAAAAA", "BBBBBBBBBBB", "DDDDDDDDDDD"})
        self.assertIn("example.com/p/one", index.urls)
        self.assertEqual(index.newest_video, dt.datetime(2026, 11, 1, 9, tzinfo=dt.timezone.utc))
        self.assertEqual(index.tags["ai"], 3)  # counted once per post
        self.assertEqual(index.tags["video"], 1)

    def test_url_forms_normalise(self):
        self.assertEqual(ap.normalize_url("https://www.Example.com/P/one/?utm=1#x"), "example.com/p/one")
        self.assertEqual(ap.normalize_url("https://youtu.be/AAAAAAAAAAA"), ap.normalize_url("https://www.youtube.com/watch?v=AAAAAAAAAAA&t=3"))
        self.assertNotEqual(ap.normalize_url("https://youtu.be/AAAAAAAAAAA"), ap.normalize_url("https://youtu.be/BBBBBBBBBBB"))

    def test_skips_videos_already_on_site_by_id_even_via_other_url_form(self):
        items = [video("AAAAAAAAAAA"), video("BBBBBBBBBBB")]
        new = ap.select_new(items, site(video_ids={"AAAAAAAAAAA"}), None)
        self.assertEqual([i.video_id for i in new], ["BBBBBBBBBBB"])

    def test_skips_blog_posts_already_linked(self):
        post = ap.Item(kind="blog", url="https://example.com/p/mine?utm=1", title="Mine", published=NOW, source="B")
        self.assertEqual(ap.select_new([post], site(urls={"example.com/p/mine"}), None), [])

    def test_same_item_from_two_sources_is_kept_once(self):
        first, second = video("AAAAAAAAAAA", title="one"), video("AAAAAAAAAAA", title="two")
        new = ap.select_new([first, second], site(), None)
        self.assertEqual([i.title for i in new], ["one"])

    def test_start_date_is_inclusive_by_day_and_newest_first(self):
        since = dt.datetime(2026, 11, 5, 18, tzinfo=dt.timezone.utc)
        early_same_day = video("AAAAAAAAAAA", published=dt.datetime(2026, 11, 5, 4, tzinfo=dt.timezone.utc))
        day_before = video("BBBBBBBBBBB", published=dt.datetime(2026, 11, 4, 23, tzinfo=dt.timezone.utc))
        later = video("CCCCCCCCCCC", published=dt.datetime(2026, 11, 9, tzinfo=dt.timezone.utc))
        new = ap.select_new([early_same_day, day_before, later], site(), since)
        self.assertEqual([i.video_id for i in new], ["CCCCCCCCCCC", "AAAAAAAAAAA"])


class PostGeneration(unittest.TestCase):
    TAGS = {"ai": 5, "grafana": 9, "observability": 4, "the context window": 3, "once only": 1, "live": 6, "video": 40}

    def test_video_post_format(self):
        item = ap.parse_transcript(TRANSCRIPT)
        item.source, item.source_tags = "Grafana YouTube channel", ["grafana labs"]
        text = ap.render_post(item, self.TAGS, CONFIG)
        expected_head = (
            '---\n'
            'title: "Build apps on your data with Grafana Pages (The Context Window #07)"\n'
            'date: 2026-11-05T04:44:12+00:00\n'
            'draft: false\n'
        )
        self.assertTrue(text.startswith(expected_head), text)
        self.assertIn('tags: ["grafana", "the context window", "ai", "observability", "english", "video", "grafana labs", "livestream"]', text)
        self.assertIn("\n---\n\nIn Build apps on your data", text)
        self.assertTrue(text.rstrip().endswith("{{< youtube TjzXIMfLSTg >}}"))

    def test_rare_and_generic_tags_not_used(self):
        item = video(title="once only live video", description="live once only")
        tags = ap.tags_for(item, self.TAGS, CONFIG)
        self.assertNotIn("once only", tags)
        self.assertNotIn("live", tags)
        self.assertEqual(tags.count("video"), 1)

    def test_blog_post_format(self):
        item = ap.Item(kind="blog", url="https://example.com/p/mine", title='Mine "quoted"', published=dt.datetime(2026, 11, 12, 9, tzinfo=dt.timezone.utc),
                       description="An excerpt about AI.", source="Context Horizon", source_tags=["context horizon"])
        text = ap.render_post(item, self.TAGS, CONFIG)
        self.assertIn('title: "Mine \\"quoted\\""', text)
        self.assertIn('tags: ["ai", "english", "context horizon"]', text)
        self.assertIn("\n\nOriginally posted [here](https://example.com/p/mine) on Context Horizon.\n\nAn excerpt about AI.\n", text)
        self.assertNotIn("youtube", text)

    def test_filename_slug_and_collisions(self):
        item = video(title="Zero to Dashboard: Grafana & Assistant! (Ünïcode)")
        taken = set()
        first = ap.filename_for(item, taken)
        self.assertEqual(first, "20261108-zero-to-dashboard-grafana-assistant-unicode.md")
        self.assertEqual(ap.filename_for(item, taken), "20261108-zero-to-dashboard-grafana-assistant-unicode-2.md")
        self.assertLessEqual(len(ap.slugify("word " * 40)), 60)

    def test_pr_title(self):
        blog = ap.Item(kind="blog", url="u", title="t", published=NOW)
        self.assertEqual(ap.pr_title([video(), video("DDDDDDDDDDD"), blog]), "New: 2 videos, 1 blog post")
        self.assertEqual(ap.pr_title([video()]), "New: 1 video")
        self.assertEqual(ap.pr_title([blog, blog]), "New: 2 blog posts")

    def test_description_never_injects_hugo_shortcodes(self):
        self.assertNotIn("{{", ap.clean_video_description("see {{< ref x >}}"))

    def test_update_home_page_changes_only_the_last_video_embed(self):
        page = ('<iframe src="https://www.youtube.com/embed/ZZZZZZZZZZZ"></iframe>\n<section id="videos">\n'
                '<iframe src="https://www.youtube.com/embed/OLDOLDOLD11" title="x"></iframe>\n</section>\n')
        with tempfile.TemporaryDirectory() as tmp:
            for relative in ap.HOME_PAGES:
                path = Path(tmp) / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(page)
            changed = ap.update_home_page(Path(tmp), "NEWNEWNEW11")
            result = (Path(tmp) / ap.HOME_PAGES[0]).read_text()
        self.assertEqual(changed, list(ap.HOME_PAGES))
        self.assertIn("embed/NEWNEWNEW11", result)
        self.assertIn("embed/ZZZZZZZZZZZ", result)
        self.assertNotIn("OLDOLDOLD11", result)


class EndToEnd(unittest.TestCase):
    def test_second_run_after_merge_finds_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, transcripts = Path(tmp) / "repo", Path(tmp) / "transcripts"
            (repo / "content" / "blog").mkdir(parents=True)
            transcripts.mkdir()
            (transcripts / "2026-11-05T04:44:12Z-x.md").write_text(TRANSCRIPT)
            for relative in ap.HOME_PAGES:
                (repo / relative).parent.mkdir(parents=True, exist_ok=True)
                (repo / relative).write_text('<section id="videos"><iframe src="https://www.youtube.com/embed/OLDOLDOLD11"></iframe></section>')
            original = ap.gather
            ap.gather = lambda args, config, now: ap.load_developer_advocacy(transcripts, config, NOW)
            self.addCleanup(setattr, ap, "gather", original)
            out = Path(tmp) / "out"
            argv = ["--repo", str(repo), "--dev-advocacy-dir", str(transcripts), "--since", "2026-11-01", "--output-dir", str(out)]
            self.assertEqual(ap.main(argv), 0)
            self.assertEqual((out / "count.txt").read_text(), "1")
            self.assertEqual((out / "pr-title.txt").read_text(), "New: 1 video")
            posts = list((repo / "content" / "blog").glob("*.md"))
            self.assertEqual(len(posts), 1)
            self.assertIn("embed/TjzXIMfLSTg", (repo / ap.HOME_PAGES[0]).read_text())
            self.assertIn("content/blog/%s" % posts[0].name, (out / "pr-body.md").read_text())
            # "Merge" the PR: the post is now on the site, so a second run is a no-op.
            self.assertEqual(ap.main(argv), 0)
            self.assertEqual((out / "count.txt").read_text(), "0")
            self.assertEqual(len(list((repo / "content" / "blog").glob("*.md"))), 1)


if __name__ == "__main__":
    unittest.main()
