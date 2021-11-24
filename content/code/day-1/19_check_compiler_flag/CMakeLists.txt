cmake_minimum_required(VERSION 3.18)

project(check_compiler_flag LANGUAGES CXX)

# we set the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# add an executable target
add_executable(asan-example asan-example.cpp)

# we set some generic compiler flags
target_compile_options(asan-example
  PUBLIC
    "-g3"
    "-O1"
  )

# FIXME include the correct CMake module to check that C++ compiler flags work
include(...)

# FIXME declare the flags to check in a new variable
set(ASAN_FLAGS ...)
# FIXME invoke check_cxx_compiler_flag
# HINT: the flags to check need to set as a CMAKE_REQUIRED_FLAGS variable

if(asan_works)
  # we transform ASAN_FLAGS to ;-separated list
  string(REPLACE " " ";" _asan_flags ${ASAN_FLAGS})
  # FIXME add the _asan_flags to the compile options of the executable target
  target_compile_options(asan-example
    ...
    )
  # this is needed for the linker to properly handle the sanitizer
  target_link_libraries(asan-example
    PUBLIC
      ${_asan_flags}
    )
endif()
