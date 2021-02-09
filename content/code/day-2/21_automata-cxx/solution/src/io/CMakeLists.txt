add_library(io)

target_sources(io
  PRIVATE
    io.cpp
  PUBLIC
    io.hpp
  )

target_include_directories(io
  PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}
  )
