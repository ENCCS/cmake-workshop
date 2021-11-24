cmake_minimum_required(VERSION 3.18)

# the project uses both C++ and C
project(check_source_runs LANGUAGES CXX C)

# we set the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# we find the UUID system library using the pkg-config utility
find_package(PkgConfig REQUIRED QUIET)
pkg_search_module(UUID REQUIRED uuid IMPORTED_TARGET)
if(TARGET PkgConfig::UUID)
  message(STATUS "Found libuuid")
endif()

# FIXME create the C++ executable from the use-uuid.cpp source file
add_executable(...)

# FIXME include the CMake module that checks whether a C source file runs
include(...)

# FIXME set the C code to test in a variable
set(...)

# FIXME perform the check
# HINT: libraries required to link are to be given in a variable called CMAKE_REQUIRED_LIBRARIES

# FIXME emit a fatal error if the check fails
if(NOT _runs)
endif()

# we finally link the library to the C++ executable
target_link_libraries(use-uuid
  PUBLIC
    PkgConfig::UUID
  )
