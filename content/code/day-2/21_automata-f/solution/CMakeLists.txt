cmake_minimum_required(VERSION 3.18)

project(automata-f LANGUAGES Fortran)

# defines targets and sources
add_subdirectory(src)

# contains an "external" library we will link to
add_subdirectory(external)
