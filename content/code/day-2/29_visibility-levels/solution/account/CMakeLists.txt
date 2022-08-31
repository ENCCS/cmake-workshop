add_library(account SHARED "")

target_sources(account
  PRIVATE
    account.cpp
  )

target_compile_options(account
  PUBLIC
    "-ffast-math"
  )

target_include_directories(account
  INTERFACE
    ${CMAKE_CURRENT_SOURCE_DIR}
  )
