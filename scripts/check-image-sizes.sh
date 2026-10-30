#!/bin/bash
# Fails when an image added or changed since BASE is larger than MAX_BYTES.
# Used by the PR workflow; works on Linux, so it checks file size only.
# Fix by running scripts/resize-images.sh on the file.
#
# Usage: scripts/check-image-sizes.sh BASE_REF
set -euo pipefail

base="${1:?usage: check-image-sizes.sh BASE_REF}"
MAX_BYTES="${MAX_BYTES:-1500000}"

status=0
while IFS= read -r -d '' f; do
  size="$(wc -c <"$f")"
  if [ "$size" -gt "$MAX_BYTES" ]; then
    echo "::error file=$f::$f is $size bytes (limit $MAX_BYTES). Run scripts/resize-images.sh $f"
    status=1
  fi
done < <(git diff --name-only --diff-filter=AM -z "$base"...HEAD -- \
  'content/assets/*.jpg' 'content/assets/*.jpeg' 'content/assets/*.png' \
  'content/assets/*.JPG' 'content/assets/*.JPEG' 'content/assets/*.PNG' \
  'content/assets/*.gif' 'content/assets/*.webp')
exit "$status"
