# needed to find the backtrace library
enable_language(C)
# needed for the random number generator
enable_language(CXX)

# verify the compatibility of the C/Fortran and C++/Fortran compilers
include(FortranCInterface)
FortranCInterface_VERIFY(CXX)

find_package(Backtrace REQUIRED)

add_library(bt-randomgen-wrap SHARED)

target_sources(bt-randomgen-wrap
  PUBLIC
    interface_backtrace.f90
    interface_randomgen.f90
  PRIVATE
    randomgen.cpp
  )

target_link_libraries(bt-randomgen-wrap
  PUBLIC
    ${Backtrace_LIBRARIES}
  )
