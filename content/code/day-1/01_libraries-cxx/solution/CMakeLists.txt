# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(libraries LANGUAGES CXX)

# generate a library from sources
add_library(message
  Message.hpp
  Message.cpp
  )

add_executable(hello-world hello-world.cpp)

target_link_libraries(hello-world PRIVATE message)
