# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name
project(ctest-will-faile LANGUAGES NONE)

# detect python
find_package(Python REQUIRED)

# define tests
enable_testing()

add_test(example ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test.py)

# we expect this test to fail
set_tests_properties(example PROPERTIES WILL_FAIL true)
