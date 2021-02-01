# set minimum cmake version
cmake_minimum_required(VERSION 3.13)

# project name and language
project(conditionals LANGUAGES CXX)

# BUILD_SHARED_LIBS is a global flag offered by CMake
# to toggle the behavior of add_library
set(BUILD_SHARED_LIBS OFF)

# list sources
list(APPEND _sources Message.hpp Message.cpp)

# generate a library from sources
add_library(message ${_sources})

add_executable(hello-world hello-world.cpp)

target_link_libraries(hello-world PRIVATE message)
