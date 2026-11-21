# nicolevanderhoeven.com

Hugo site, built with `hugo --minify` (Hugo 0.169.0 extended) and deployed by `.github/workflows/deploy.yml`.

## Images

Photos under `content/assets` are published as is, so keep them at most 1600 px wide. Enable the pre-commit hook once per clone and it resizes staged JPEG and PNG files for you (macOS, uses `sips`):

    git config core.hooksPath scripts/hooks

To resize files by hand, run `scripts/resize-images.sh FILE...`. The PR workflow fails when an added or changed JPEG or PNG is larger than 1.5 MB and wider than 1600 px, which is exactly what `resize-images.sh` can fix. Other oversized images (GIF, WebP, or JPEG/PNG already 1600 px wide or less) only produce a warning and need manual optimisation.

## Automatic posts

`.github/workflows/auto-posts.yml` runs daily (06:17 UTC) and on demand (Actions tab, "Auto posts", "Run workflow"). It looks for Nicole's new videos and blog posts and opens **one** pull request, titled like "New: 2 videos, 1 blog post", with one post per item. It never merges and never pushes to `master`; the branch is `auto/new-posts`. If nothing is new it does nothing. While the PR is open, each run refreshes it; merge or close it before editing the generated posts by hand, because a later run rebuilds the branch.

What it checks (the PR body lists them again):

- **Grafana channel videos**: the transcripts in [grafana/developer-advocacy](https://github.com/grafana/developer-advocacy/tree/main/transcripts) (public, read through a sparse checkout, no token). A video counts as Nicole's when her name appears in its title, description or summary (case-insensitive, tolerating spacing and spelling variants such as "Nicole Vanderhoeven", "Nicole Vanderhovven" and "nicolevdh"). The transcript text itself is never searched.
- **Nicole's own channel**: the public RSS feed of channel `UCrmQZ9HHnJ2qpd6udc8iYYw` (public videos only).
- **Blog feeds** (`blog_feeds` in `scripts/auto_posts/config.json`): the Grafana Labs blog (`grafana.com/blog/index.xml`, only posts whose author is Nicole), Context Horizon (`contexthorizon.substack.com/feed`, only posts by Nicole) and her Medium profile (`medium.com/feed/@n_vanderhoeven`). Grafana's blog has no per-author feed, and its feed only holds the latest 10 posts, which is plenty for a daily run.

Skipped: anything already on the site (a YouTube video id or a URL that already appears in `content/`), private, deleted or not yet public videos, and anything published before the start date. The start date defaults to the date of the newest post that embeds a YouTube video; override it with `--since YYYY-MM-DD` or the `since` input of the manual run.

Each post copies the format of the existing ones (front matter, `{{< youtube ID >}}` embed, or "Originally posted [here](URL) on Source." for blog posts) and uses only the source's title, date and description or summary: no AI-written text and no API keys. Tags are limited to tags already used on at least two posts, found in the title, description or summary, plus `english`, `video`, `grafana labs`, and `livestream` plus the show name for recognised shows. Descriptions in developer-advocacy are truncated by YouTube (they end in "..."), so edit the intro before merging if you want a fuller one. The PR also points the home page's Last Video embed (`layouts/index.html`, and the theme's copy) at the newest new video.

Setup notes:

- Settings, Actions, General: tick "Allow GitHub Actions to create and approve pull requests".
- PRs opened with the default `GITHUB_TOKEN` do not start the "PR checks" workflow. To get it, add a repository secret `AUTO_POSTS_TOKEN` (a fine-grained token with contents and pull-requests write); the workflow uses it when present.
- Permissions are `contents: write` and `pull-requests: write` only; the third-party action is pinned to a commit SHA.

Run it by hand (Python 3 only, standard library):

    git clone --depth 1 https://github.com/grafana/developer-advocacy.git /tmp/developer-advocacy
    python3 scripts/auto_posts/auto_posts.py --dev-advocacy-dir /tmp/developer-advocacy/transcripts --dry-run
    # drop --dry-run to write the posts and update the home page; add --since 2026-11-01 to override the start date

Unit tests (matching, de-duplication, post generation):

    python3 -m unittest discover -s scripts/auto_posts/tests -v
