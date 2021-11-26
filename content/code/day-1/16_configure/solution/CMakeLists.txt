# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(processor LANGUAGES CXX)

add_executable(processor-info processor-info.cpp)

include(CMakePrintHelpers)

foreach(key
  IN ITEMS
    NUMBER_OF_PHYSICAL_CORES
    TOTAL_PHYSICAL_MEMORY
    OS_NAME
    OS_PLATFORM
  )
  # query the item ${key} and save its value in the variable _${key}
  # i.e. the value of NUMBER_OF_LOGICAL_CORES will be saved in _NUMBER_OF_LOGICAL_CORES
  cmake_host_system_information(RESULT _${key} QUERY ${key})
  cmake_print_variables(_${key})
endforeach()

# and its include directories
target_include_directories(processor-info
  PRIVATE
    ${PROJECT_BINARY_DIR}
  )

# configure the file
configure_file(config.h.in config.h @ONLY)
