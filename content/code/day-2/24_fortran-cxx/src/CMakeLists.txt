add_subdirectory(interfaces)
add_subdirectory(utils)

# FIXME create an executable from the Fortran source file
add_executable(...)

# FIXME link the Fortran executable to the libraries
target_link_libraries(bt-randomgen-example
  PRIVATE
    ...
  )
