# nicolevanderhoeven.com

Hugo site, built with `hugo --minify` (Hugo 0.169.0 extended) and deployed by `.github/workflows/deploy.yml`.

## Images

Photos under `content/assets` are published as is, so keep them at most 1600 px wide. Enable the pre-commit hook once per clone and it resizes staged JPEG and PNG files for you (macOS, uses `sips`):

    git config core.hooksPath scripts/hooks

To resize files by hand, run `scripts/resize-images.sh FILE...`. The PR workflow fails when an added or changed image is larger than 1.5 MB.
