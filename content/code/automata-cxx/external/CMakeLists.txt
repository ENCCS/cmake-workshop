add_library(conversion)

target_sources(conversion
  PRIVATE
    conversion.cpp
  PUBLIC
    conversion.hpp
  )

target_include_directories(conversion
  PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}
  )
