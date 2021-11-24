# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(mpi-f LANGUAGES Fortran)

find_package(MPI REQUIRED COMPONENTS Fortran)

add_executable(hello-mpi hello-mpi.f90)

target_link_libraries(hello-mpi
  PRIVATE
    MPI::MPI_Fortran
  )
