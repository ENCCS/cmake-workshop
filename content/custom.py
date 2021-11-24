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
    "find_file",
    "find_path",
    "find_library",
    "find_program",
    "target_include_directories",
    "target_link_libraries",
    "target_compile_options",
    "target_compile_definitions",
    "message",
    "option",
    "if",
    "foreach",
    "cmake_host_system_information",
    "configure_file",
    "execute_process",
    "add_custom_command",
    "try_compile",
    "try_run",
    "add_test",
    "set_tests_properties",
    "file",
    "set",
    "include",
    "get_property",
    "set_property",
    "get_target_property",
    "set_target_properties",
    "add_custom_target",
]

CTERM = """
.. |{command}| raw:: html

   <a class="reference internal" href="https://cmake.org/cmake/help/latest/command/{command}.html"><span class="xref std std-term"><code class="docutils literal notranslate">{command}</code></span></a>
"""

VARIABLES = [
    "PROJECT_BINARY_DIR",
    "PROJECT_SOURCE_DIR",
    "CMAKE_CURRENT_LIST_DIR",
    "CMAKE_CURRENT_SOURCE_DIR",
]

VTERM = """
.. |{variable}| raw:: html

   <a class="reference internal" href="https://cmake.org/cmake/help/latest/variable/{variable}.html"><span class="xref std std-term"><code class="docutils literal notranslate">{variable}</code></span></a>
"""

COMMANDS_IN_MODULES = [
    ("cmake_print_variables", "CMakePrintHelpers"),
    ("check_cxx_source_compiles", "CheckCXXSourceCompiles"),
    ("check_cxx_compiler_flag", "CheckCXXCompilerFlag"),
    ("check_c_source_runs", "CheckCSourceRuns"),
    ("cmake_dependent_option", "CMakeDependentOption"),
    ("pkg_search_module", "FindPkgConfig"),
    ("FetchContent_Declare", "FetchContent"),
    ("FetchContent_MakeAvailable", "FetchContent"),
    ("FortranCInterface_VERIFY", "FortranCInterface"),
    ("FortranCInterface_HEADER", "FortranCInterface"),
]

CinMTERM = """
.. |{command}| raw:: html

   <a class="reference internal" href="https://cmake.org/cmake/help/latest/module/{module}.html"><span class="xref std std-term"><code class="docutils literal notranslate">{command}</code></span></a>
"""


def cmake_glossary():
    commands = "\n".join((CTERM.format(command=x) for x in COMMANDS))
    variables = "\n".join((VTERM.format(variable=x) for x in VARIABLES))
    commands_in_modules = "\n".join(
        (CinMTERM.format(command=x[0], module=x[1]) for x in COMMANDS_IN_MODULES)
    )
    return commands + variables + commands_in_modules
