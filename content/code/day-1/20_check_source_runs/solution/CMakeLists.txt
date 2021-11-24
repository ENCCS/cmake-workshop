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

# create a C++ executable using UUID
add_executable(use-uuid use-uuid.cpp)

# now check that we can use UUID properly
include(CheckCSourceRuns)

# set the C code to test in a variable
set(_test_uuid
  "
#include <uuid/uuid.h>

int main(int argc, char * argv[]) {
  uuid_t uuid;

  uuid_generate(uuid);

  return 0;
}
  ")

set(CMAKE_REQUIRED_LIBRARIES PkgConfig::UUID)
check_c_source_runs("${_test_uuid}" _runs)
unset(CMAKE_REQUIRED_LIBRARIES)

if(NOT _runs)
  message(FATAL_ERROR "Cannot run a simple C executable using libuuid!")
endif()

# we finally link the library to the C++ executable
target_link_libraries(use-uuid
  PUBLIC
    PkgConfig::UUID
  )
