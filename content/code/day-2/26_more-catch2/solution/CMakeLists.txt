# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(more-catch2 LANGUAGES CXX)

# require C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# example library
add_library(sum_integers sum_integers.cpp)

# main code
add_executable(sum_up main.cpp)
target_link_libraries(sum_up PRIVATE sum_integers)

# enable FetchContent
include(FetchContent)

# declare Catch2
FetchContent_Declare(Catch2                              # name of the content
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git  # the repository
  GIT_TAG        v2.13.4                                 # the tag
  )

# make available
FetchContent_MakeAvailable(Catch2)

# testing binary
add_executable(cpp_test test.cpp)
target_link_libraries(cpp_test PRIVATE sum_integers Catch2::Catch2)

# enable testing functionality
enable_testing()

# define test
add_test(
  NAME catch_test
  COMMAND $<TARGET_FILE:cpp_test> --success
  )
