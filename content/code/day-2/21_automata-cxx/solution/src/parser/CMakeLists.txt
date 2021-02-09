add_library(parser)

target_sources(parser
  PRIVATE
    parser.cpp
  PUBLIC
    parser.hpp
  )

target_include_directories(parser
  PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}
  )
