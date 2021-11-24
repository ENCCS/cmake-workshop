cmake_minimum_required(VERSION 3.18)

project(find_cffi LANGUAGES NONE)

find_package(Python REQUIRED)

execute_process(
  COMMAND
    # FIXME provide the Python command
  OUTPUT_VARIABLE
    # FIXME provide a variable for capturing the standard output stream
  ERROR_VARIABLE
    # FIXME provide a variable for capturing the standard error stream
  OUTPUT_STRIP_TRAILING_WHITESPACE
  ERROR_STRIP_TRAILING_WHITESPACE
  )

# FIXME print out the contents of the standard output and standard error streams
# FIXME quit if "ModuleNotFoundError" is in the standard error stream
# HINT: use the MATCHES operator to search in the string
