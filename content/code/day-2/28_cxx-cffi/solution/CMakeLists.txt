# define minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and supported language
project(bank LANGUAGES CXX C)

# require C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# require python
find_package(Python 3.6 REQUIRED Interpreter Development)

# interface and sources
add_subdirectory(account)

# turn on testing
enable_testing()

# copy test.py to root build folder
file(COPY account/test.py DESTINATION ${PROJECT_BINARY_DIR})

# define test
add_test(
  NAME
    python_test
  COMMAND
    ${Python_EXECUTABLE} ${PROJECT_BINARY_DIR}/test.py
  )
