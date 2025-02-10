#! /bin/bash

set -e

if [ -z "$1" ]; then
  echo "Need a bib file to import"
  exit 1
fi

PUB_DIR=/home/adria/dev/projects/trfclab.org/trfclab-v2/content/publication

academic import --bibtex "$1" --publication-dir "$PUB_DIR" --compact

for dir in "$PUB_DIR"/*/; do
  echo "Directory: $dir"
  sed -E -i "s/- '2'/- 'article-journal'/" "$dir"index.md
  cp "$dir"index.md "$dir"index.ca.md
  cp "$dir"index.md "$dir"index.es.md
done

