#!/usr/bin/env bash
set -euo pipefail


examples="$(find . -maxdepth 1 -mindepth 1 -type d)"

echo $examples

for dir in $examples; do
    echo "$dir"
    # make tarball exercises
    tar caf "$dir".tar.bz2 --exclude="CMakeLists.txt" "$dir"
    # make tarball solutions
    tar caf "$dir"_solution.tar.bz2 "$dir"
done
