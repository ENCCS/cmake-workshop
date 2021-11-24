# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(cxx-fortran LANGUAGES CXX C Fortran)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(src)
