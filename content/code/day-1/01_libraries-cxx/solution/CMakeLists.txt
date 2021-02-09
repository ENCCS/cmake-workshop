# set minimum cmake version
cmake_minimum_required(VERSION 3.13)

# project name and language
project(libraries LANGUAGES CXX)

# generate a library from sources
add_library(message
  STATIC
    Message.hpp
    Message.cpp
  )

add_executable(hello-world hello-world.cpp)

target_link_libraries(hello-world PRIVATE message)
