# -*- coding: utf-8 -*-

from sphinx_lesson.directives import _BaseCRDirective


class SignatureDirective(_BaseCRDirective):
    extra_classes = ["toggle-shown", "dropdown"]


class ParametersDirective(_BaseCRDirective):
    extra_classes = ["dropdown"]


class TypealongDirective(_BaseCRDirective):
    extra_classes = ["toggle-shown", "dropdown"]


DIRECTIVES = [SignatureDirective, ParametersDirective, TypealongDirective]

COMMANDS = [
    "cmake_minimum_required",
    "project",
    "add_subdirectory",
    "add_library",
    "add_executable",
    "target_sources",
    "find_package",
    "target_include_directories",
    "target_link_libraries",
    "target_compile_options",
    "target_compile_definitions",
]

TERM = """
.. |{command}| raw:: html

   <a class="reference internal" href="https://cmake.org/cmake/help/latest/command/{command}.html"><span class="xref std std-term"><code class="docutils literal notranslate">{command}</code></span></a>
"""


def cmake_commands():
    return "\n".join([TERM.format(command=x) for x in COMMANDS])
