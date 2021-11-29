#!/usr/bin/env python3

from pathlib import Path
from subprocess import check_output

from cffi import FFI

ffibuilder = FFI()

definitions = ["-DACCOUNT_API=", "-DACCOUNT_NOINCLUDE"]
header = Path(__file__).resolve().parent / "account.h"
command = ["cc", "-E"] + definitions + [str(header)]
interface = check_output(command).decode("utf-8")

# remove possible \r characters on windows which
# would confuse cdef
_interface = [l.strip("\r") for l in interface.split("\n")]

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("\n".join(_interface))

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declared functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source(
    "_pyaccount",
    """
     #include "account.h"
""",
)

ffibuilder.emit_c_code("_pyaccount.c")
