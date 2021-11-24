# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name
project(ctest-labels LANGUAGES NONE)

# detect python
find_package(Python REQUIRED)

# define tests
enable_testing()

add_test(
  NAME feature-a
  COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test/feature-a.py
  )

add_test(
  NAME feature-b
  COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test/feature-b.py
  )

add_test(
  NAME feature-c
  COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test/feature-c.py
  )

add_test(
  NAME feature-d
  COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test/feature-d.py
  )

add_test(
  NAME benchmark-a
  COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test/benchmark-a.py
  )

add_test(
  NAME benchmark-b
  COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test/benchmark-b.py
  )

set_tests_properties(
  feature-a
  feature-b
  feature-c
  PROPERTIES
    LABELS "quick"
  )

set_tests_properties(
  feature-d
  benchmark-a
  benchmark-b
  PROPERTIES
    LABELS "long"
  )
