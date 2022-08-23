add_library(initial)

target_sources(initial
  PRIVATE
    initial.f90
  )

target_include_directories(initial
  INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
  )
