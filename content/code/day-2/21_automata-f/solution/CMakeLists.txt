cmake_minimum_required(VERSION 3.14)

project(automata-f LANGUAGES Fortran)

# defines targets and sources
add_subdirectory(src)

# contains an "external" library we will link to
add_subdirectory(external)
