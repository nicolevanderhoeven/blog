#!/bin/bash
# Shrinks JPEG and PNG images so no photo is published wider than MAX_WIDTH
# pixels. Files are re-encoded in place, so URLs and filenames never change.
# Needs macOS `sips`. GIF, SVG, WebP and PDF files are left alone.
#
# Usage: scripts/resize-images.sh FILE...
# Prints one line per file it shrank. A file is only replaced when the result
# is smaller than the original.
set -euo pipefail

MAX_WIDTH="${MAX_WIDTH:-1600}"
JPEG_QUALITY="${JPEG_QUALITY:-80}"

command -v sips >/dev/null || { echo "resize-images: sips not found (macOS only)" >&2; exit 1; }

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

for f in "$@"; do
  case "$(printf '%s' "${f##*.}" | tr '[:upper:]' '[:lower:]')" in
    jpg|jpeg) kind=jpeg ;;
    png) kind=png ;;
    *) continue ;;
  esac
  [ -f "$f" ] || continue

  width="$(sips -g pixelWidth "$f" | awk '/pixelWidth/ {print $2}')"
  height="$(sips -g pixelHeight "$f" | awk '/pixelHeight/ {print $2}')"
  orient="$(sips -g orientation "$f" | awk '/orientation/ {print $2}')"
  # EXIF orientations 5-8 are rotated 90 degrees: the displayed width is the stored height.
  case "$orient" in 5|6|7|8) width="$height" ;; esac
  [ "$width" -gt "$MAX_WIDTH" ] || continue

  out="$tmp/out.$kind"
  if [ "$kind" = jpeg ]; then
    sips -s format jpeg -s formatOptions "$JPEG_QUALITY" "$f" --out "$out" >/dev/null
  else
    cp "$f" "$out"
  fi
  # Resample along the stored width or height, whichever is the displayed width.
  case "$orient" in
    5|6|7|8) sips --resampleHeight "$MAX_WIDTH" "$out" >/dev/null ;;
    *) sips --resampleWidth "$MAX_WIDTH" "$out" >/dev/null ;;
  esac

  before="$(wc -c <"$f")"
  after="$(wc -c <"$out")"
  if [ "$after" -lt "$before" ]; then
    cat "$out" >"$f"
    echo "resized $f: $before -> $after bytes"
  fi
  rm -f "$out"
done
