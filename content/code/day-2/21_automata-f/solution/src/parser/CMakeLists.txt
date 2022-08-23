add_library(parser)

target_sources(parser
  PRIVATE
    parser.f90
  )

target_include_directories(parser
  INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
  )
