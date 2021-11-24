# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(hello-ctest LANGUAGES CXX)

# require C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# example library
add_library(sum_integers sum_integers.cpp)

# main code
add_executable(sum_up main.cpp)
target_link_libraries(sum_up PRIVATE sum_integers)

# testing binary
add_executable(cpp_test test.cpp)
target_link_libraries(cpp_test PRIVATE sum_integers)

# enable testing functionality
enable_testing()

# define tests
add_test(
  NAME cpp_test
  COMMAND $<TARGET_FILE:cpp_test>
  )
