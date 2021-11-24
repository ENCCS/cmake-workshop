# FIXME create library from sources in this folder
add_library(...)

# add this folder to include directories for the project
target_include_directories(conversion
  PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}
  )
