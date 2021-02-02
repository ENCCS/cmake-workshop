#!/usr/bin/env bash
set -euo pipefail

mkdir -p tarballs

examples="$(find . -maxdepth 1 -mindepth 1 -type d -not -path './tarballs')"

echo $examples

for dir in $examples; do
    echo "$dir"
    # make tarball exercises
    tar caf "$dir".tar.bz2 --exclude="CMakeLists.txt" "$dir"
    # make tarball solutions
    tar caf "$dir"_solution.tar.bz2 "$dir"
done

# move tarballs to separate folder
mv *.tar.bz2 tarballs
