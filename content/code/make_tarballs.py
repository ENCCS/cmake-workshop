#!/usr/bin/env python3

from pathlib import Path

import tarfile


# create tarballs folder
out = Path("tarballs")
out.mkdir(parents=True, exist_ok=True)

# find exercises
exercises = [
    x
    for x in list(Path("day-1").iterdir()) + list(Path("day-2").iterdir())
    if x.is_dir()
]

# prepare .tar.bz2 for scaffolds
print("Preparing .tar.bz2 for scaffolds")
for ex in exercises:
    fs = [y for y in ex.iterdir() if y.name != "solution"]
    with tarfile.open(out / f"{ex.name}.tar.bz2", "w:bz2") as t:
        for f in fs:
            t.add(f)

# prepare .tar.bz2 for solutions
print("Preparing .tar.bz2 for solutions")
for ex in exercises:
    fs = [y for y in (ex / "solution").iterdir()]
    with tarfile.open(out / f"{ex.name}_solution.tar.bz2", "w:bz2") as t:
        for f in fs:
            t.add(f)
