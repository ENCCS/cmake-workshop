# define minimum cmake version
cmake_minimum_required(VERSION 3.18)

# FIXME declare a project using CXX 
project(bank ...)

# FIXME require python package. We will need the interpreter and development
# components
find_package(Python ...)

# FIXME add account subdirectory
add_subdirectory(...)

# FIXME turn on testing
...

# copy test.py to root build folder
file(COPY account/test.py DESTINATION ${PROJECT_BINARY_DIR})

# FIXME define test to run test.py
add_test(
  NAME
    ...
  COMMAND
    ${Python_EXECUTABLE} ...
  )
