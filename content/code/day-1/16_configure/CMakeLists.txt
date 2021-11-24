# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(processor LANGUAGES CXX)

add_executable(processor-info processor-info.cpp)

include(CMakePrintHelpers)

foreach(key
  IN ITEMS
    ...
  )
  # query the item ${key} and save its value in the variable _${key}
  # i.e. the value of NUMBER_OF_LOGICAL_CORES will be saved in _NUMBER_OF_LOGICAL_CORES
  cmake_host_system_information(RESULT ... QUERY ...)
  cmake_print_variables(...)
endforeach()

# and PPROJECT_BINARY_DIR as its include directories
target_include_directories(processor-info
	...
  )

# configure the file
configure_file(... ... @ONLY)
