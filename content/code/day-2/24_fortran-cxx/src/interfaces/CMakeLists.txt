# FIXME verify the compatibility of the C/Fortran and C++/Fortran compilers
include(...)

find_package(Backtrace REQUIRED)

# FIXME create library from sources
add_library(...)

# FIXME add sources to library
target_sources(bt-randomgen-wrap
  PUBLIC
    ...
  PRIVATE
    ...
  )

target_link_libraries(bt-randomgen-wrap
  PUBLIC
    ${Backtrace_LIBRARIES}
  )
