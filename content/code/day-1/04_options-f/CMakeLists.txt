# FIXME set minimum cmake version
cmake_minimum_required(...)

# FIXME project name and language
project(libraries ...)

# FIXME expose options to the user
option(...)

message(STATUS "Compile sources into a library? ${USE_LIBRARY}")

include(CMakeDependentOption)

# FIXME second option depends on the value of the first
cmake_dependent_option(
  MAKE_STATIC_LIBRARY ...)

# FIXME third option depends on the value of the first
cmake_dependent_option(
  MAKE_SHARED_LIBRARY ...)

if(USE_LIBRARY)
  message(STATUS "Compile sources into a STATIC library? ${MAKE_STATIC_LIBRARY}")
  message(STATUS "Compile sources into a SHARED library? ${MAKE_SHARED_LIBRARY}")

  # FIXME create executable from hello-world.f90
  add_executable(hello-world ...)

  if(MAKE_SHARED_LIBRARY)
    # FIXME create a shared library
    add_library(message-shared ...)

    # FIXME link executable to shared library
    target_link_libraries(hello-world ...)
  endif()

  if(MAKE_STATIC_LIBRARY)
    # FIXME create a static library
    add_library(message-static ...)

    # FIXME link executable to static library
    target_link_libraries(hello-world ...)
  endif()
else()
  # FIXME create executable from all sources
  add_executable(hello-world ...)
endif()
