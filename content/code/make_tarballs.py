#!/usr/bin/env python3

from pathlib import Path

import tarfile


# create tarballs folder
out = Path("tarballs")
out.mkdir(parents=True, exist_ok=True)

# folders from which to strip the CMakeLists.txt before tarball-ing
challenges = [
    "conditionals-cxx",
    "conditionals-f",
    "hello-cxx",
    "hello-f",
    "libraries-cxx",
    "libraries-f",
    "loops-cxx",
    "options-cxx",
    "options-f",
    "host_system_information",
    "configure",
]

# folders to tarballs directly
typealongs = [
    "OS",
    "processor",
    "sys_preproc",
]

# all complete examples
examples = challenges + typealongs

for d in examples:
    with tarfile.open(out / f"{d}_solution.tar.bz2", "w:bz2") as t:
        t.add(d)


for d in challenges:
    # filter out any CMakeLists.txt in any subfolder
    fs = [x for x in Path(d).iterdir() if x.name != "CMakeLists.txt"]
    with tarfile.open(out / f"{d}.tar.bz2", "w:bz2") as t:
        for f in fs:
            t.add(f)
