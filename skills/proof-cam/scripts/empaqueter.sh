#!/bin/bash
# Fabrique proof-cam.zip, le fichier à installer comme skill.
# À relancer après toute modification de la fiche, du gabarit ou du skill.
#   bash scripts/empaqueter.sh
set -euo pipefail
skill="$(cd "$(dirname "$0")/.." && pwd)"
sortie="$(dirname "$skill")/proof-cam.zip"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

node "$skill/scripts/verifier-jetons.mjs"

rsync -a "$skill/" "$tmp/proof-cam/" \
  --exclude '.*' --exclude 'renders' --exclude 'snapshots' --exclude 'export-*.html' --exclude 'node_modules'
# Le studio HyperFrames marque les éléments qu'il a vus : on retire ces repères du paquet.
find "$tmp/proof-cam/gabarit" -name '*.html' -exec sed -i '' -E 's/ data-hf-id="[^"]*"//g' {} +

rm -f "$sortie"
(cd "$tmp" && zip -qr "$sortie" proof-cam)
echo "Paquet prêt : $sortie ($(du -h "$sortie" | cut -f1 | tr -d ' '))"
