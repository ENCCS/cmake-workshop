find_package(BLAS REQUIRED)
find_package(LAPACK REQUIRED)

# FIXME include CMake module for C/C++ and Fortran interoperability
include(...)

# FIXME verify compatibility of compilers

# FIXME generate Fortran name mangling header
FortranCInterface_HEADER(
  ...
  SYMBOLS ...
  )

add_library(math)

target_sources(math
  PRIVATE
    CxxBLAS.cpp
    CxxLAPACK.cpp
  )

# FIXME define include directories for dependents on math library
target_include_directories(math
  ...
  )

target_link_libraries(math
  PUBLIC
    LAPACK::LAPACK
  )
