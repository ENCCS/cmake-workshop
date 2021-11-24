# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(mpi-cxx LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(MPI REQUIRED COMPONENTS CXX)

add_executable(hello-mpi hello-mpi.cpp)

target_link_libraries(hello-mpi
  PUBLIC
    MPI::MPI_CXX
  )
