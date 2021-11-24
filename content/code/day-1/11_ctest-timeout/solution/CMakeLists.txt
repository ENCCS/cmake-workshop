# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name
project(ctest-timeout LANGUAGES NONE)

# detect python
find_package(Python REQUIRED)

# define tests
enable_testing()

# we expect this test to run for 2 seconds
add_test(example ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test.py)

# timeout for this test set to 10 seconds
set_tests_properties(example PROPERTIES TIMEOUT 10)
