# set minimum cmake version
cmake_minimum_required(VERSION 3.13)

# project name and language
project(mpi-f LANGUAGES Fortran)

# FIXME find MPI with Fortran component

add_executable(hello-mpi hello-mpi.f90)

# FIXME link hello-mpi with imported target
target_link_libraries(hello-mpi
	...
  )
