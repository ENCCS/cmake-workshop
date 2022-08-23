add_library(io)

target_sources(io
  PRIVATE
    io.f90
  )

target_include_directories(io
  INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
  )
