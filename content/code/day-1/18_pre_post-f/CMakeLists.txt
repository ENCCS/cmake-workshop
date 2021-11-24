cmake_minimum_required(VERSION 3.18)

project(pre_post LANGUAGES Fortran)

find_package(Python REQUIRED)

# we default to Release build type
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()

add_executable(example)

target_sources(example
  PRIVATE
    example.f90
  )

add_custom_command(
  TARGET
    # FIXME add the target name
  PRE_LINK
  COMMAND
    # FIXME call echo-file.py through Python to read the file CMakeFiles/example.dir/link.txt
    ${Python_EXECUTABLE}
      ...
  COMMENT
    "link line:"
  VERBATIM
  )

add_custom_command(
  TARGET
    # FIXME add the target name
  POST_BUILD
  COMMAND
    # FIXME call static-size.py through Python on the produced executable
    ${Python_EXECUTABLE}
      ...
  COMMENT
    "static size of executable:"
  VERBATIM
  )
