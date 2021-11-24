# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(conditionals LANGUAGES Fortran)

set(MAKE_SHARED_LIBRARY OFF)

if(MAKE_SHARED_LIBRARY)
  message(STATUS "Build shared library")
  add_library(message SHARED message.f90)
else()
  message(STATUS "Build static library")
  add_library(message STATIC message.f90) 
endif()

add_executable(hello-world hello-world.f90)

target_link_libraries(hello-world PRIVATE message)
