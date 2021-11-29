# define minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and supported language
project(cxx-python LANGUAGES CXX)

# require C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# find Python interpreter and header files
find_package(Python 3.6 REQUIRED COMPONENTS Interpreter Development)

# turn on testing
enable_testing()

add_subdirectory(account)
