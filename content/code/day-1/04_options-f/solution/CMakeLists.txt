# set minimum cmake version
cmake_minimum_required(VERSION 3.14)

# project name and language
project(libraries LANGUAGES Fortran)

# expose options to the user
option(USE_LIBRARY "Compile sources into a library" OFF)

message(STATUS "Compile sources into a library? ${USE_LIBRARY}")

include(CMakeDependentOption)

# second option depends on the value of the first
cmake_dependent_option(
  MAKE_STATIC_LIBRARY "Compile sources into a static library" OFF
  "USE_LIBRARY" ON
  )

# third option depends on the value of the first
cmake_dependent_option(
  MAKE_SHARED_LIBRARY "Compile sources into a shared library" ON
  "USE_LIBRARY" ON
  )

if(USE_LIBRARY)
  message(STATUS "Compile sources into a STATIC library? ${MAKE_STATIC_LIBRARY}")
  message(STATUS "Compile sources into a SHARED library? ${MAKE_SHARED_LIBRARY}")

  if(MAKE_SHARED_LIBRARY)
    add_library(message SHARED message.f90)

    add_executable(hello-world hello-world.f90)

    target_link_libraries(hello-world PRIVATE message)
  endif()

  if(MAKE_STATIC_LIBRARY)
    add_library(message STATIC message.f90)

    add_executable(hello-world hello-world.f90)

    target_link_libraries(hello-world PRIVATE message)
  endif()
else()
  add_executable(hello-world hello-world.f90 message.f90)
endif()
