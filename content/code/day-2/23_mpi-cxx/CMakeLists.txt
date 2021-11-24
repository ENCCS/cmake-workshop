# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(mpi-cxx LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# FIXME find MPI with C++ component

add_executable(hello-mpi hello-mpi.cpp)

# FIXME link hello-mpi with the imported targett
target_link_libraries(hello-mpi
     ...
  )
