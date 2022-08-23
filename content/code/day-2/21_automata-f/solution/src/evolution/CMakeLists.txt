add_library(evolution)

target_sources(evolution
  PRIVATE
    empty.f90
    ancestors.f90
    evolution.f90
  )

target_include_directories(evolution
  INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
  )
