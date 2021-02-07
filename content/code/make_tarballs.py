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
    "pre_post-f",
    "ctest-will-fail",
    "ctest-timeout",
    "automata-cxx",
    "automata-f",
    "mpi-cxx",
    "mpi-f",
    "ctest-catch2",
]

# folders to tarballs directly
typealongs = [
    "OS",
    "processor",
    "sys_preproc",
    "hello-ctest",
    "taskloop",
]

# folders that require manual intervention for tarballing, e.g. to provide a meaningful scaffold
manual = [
    "find_cffi",
    "check_compiler_flag",
    "check_source_runs",
    "ctest-labels",
    "ctest-cost",
    "more-catch2",
    "fortran-cxx",
    "cxx-fortran",
]


# all complete examples
examples = challenges + typealongs + manual

for d in examples:
    # filter out build folders
    fs = [x for x in Path(d).iterdir() if x.name != "build"]
    with tarfile.open(out / f"{d}_solution.tar.bz2", "w:bz2") as t:
        for f in fs:
            t.add(f)


for d in challenges:
    # filter out build folders and any CMakeLists.txt in any subfolder
    fs = [x for x in Path(d).iterdir() if not (x.name == "build" or x.name == "CMakeLists.txt")]
    with tarfile.open(out / f"{d}.tar.bz2", "w:bz2") as t:
        for f in fs:
            t.add(f)

for d in manual:
    print(f"Scaffold for folder {d} needs to be manually tarball-ed!!")
