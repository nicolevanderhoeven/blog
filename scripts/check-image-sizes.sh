#!/bin/bash
# Fails when a JPEG or PNG added or changed since BASE is larger than MAX_BYTES
# and wider than MAX_WIDTH pixels: those are the files scripts/resize-images.sh
# can shrink. Any other oversized image (GIF, WebP, or a JPEG/PNG that is
# already narrow enough) only gets a warning, since it needs manual optimisation.
# Used by the PR workflow; works on Linux and needs ImageMagick `identify`.
#
# Usage: scripts/check-image-sizes.sh BASE_REF
set -euo pipefail

base="${1:?usage: check-image-sizes.sh BASE_REF}"
MAX_BYTES="${MAX_BYTES:-1500000}"
MAX_WIDTH="${MAX_WIDTH:-1600}"

command -v identify >/dev/null || { echo "check-image-sizes: identify not found (install ImageMagick)" >&2; exit 1; }

status=0
while IFS= read -r -d '' f; do
  size="$(wc -c <"$f")"
  [ "$size" -gt "$MAX_BYTES" ] || continue

  case "$(printf '%s' "${f##*.}" | tr '[:upper:]' '[:lower:]')" in
    jpg|jpeg|png)
      read -r orient width height < <(identify -format '%[orientation] %w %h\n' "$f[0]")
      # EXIF orientations 5-8 are rotated 90 degrees: the displayed width is the stored height.
      case "$orient" in LeftTop|RightTop|RightBottom|LeftBottom) width="$height" ;; esac
      if [ "$width" -gt "$MAX_WIDTH" ]; then
        echo "::error file=$f::$f is $size bytes and $width px wide (limits $MAX_BYTES bytes, $MAX_WIDTH px). Run scripts/resize-images.sh $f"
        status=1
        continue
      fi
      ;;
  esac
  echo "::warning file=$f::$f is $size bytes (limit $MAX_BYTES) but cannot be fixed by scripts/resize-images.sh. Optimise it manually."
done < <(git diff --name-only --diff-filter=AM -z "$base"...HEAD -- \
  'content/assets/*.jpg' 'content/assets/*.jpeg' 'content/assets/*.png' \
  'content/assets/*.JPG' 'content/assets/*.JPEG' 'content/assets/*.PNG' \
  'content/assets/*.gif' 'content/assets/*.webp')
exit "$status"
