# create folder for generated code
file(MAKE_DIRECTORY ${PROJECT_BINARY_DIR}/generated)

# Call CFFI to generate bindings source file _pyaccount.c
add_custom_command(
  OUTPUT
    ${PROJECT_BINARY_DIR}/generated/_pyaccount.c
  COMMAND
    ${Python_EXECUTABLE} ${CMAKE_CURRENT_LIST_DIR}/cffi_builder.py
  MAIN_DEPENDENCY
    ${CMAKE_CURRENT_LIST_DIR}/cffi_builder.py
  DEPENDS
    ${CMAKE_CURRENT_LIST_DIR}/account.h
  WORKING_DIRECTORY
    ${PROJECT_BINARY_DIR}/generated
  )

add_custom_target(
  pyaccount-builder
  ALL
  DEPENDS
    ${PROJECT_BINARY_DIR}/generated/_pyaccount.c
  )

# FIXME add python module from Fortran implementation and generated C wrapper 
Python_add_library(_pyaccount
  MODULE
    ...
  )

# add dependency between _pyaccount target and pyaccount-builder custom target
add_dependencies(_pyaccount pyaccount-builder)

target_include_directories(_pyaccount
  PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}  # where account.h lives
    ${CMAKE_CURRENT_BINARY_DIR}  # where account_export.h lives
  )

# copy __init__.py to build folder
file(COPY __init__.py DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

# generate account_export.h
include(GenerateExportHeader)
generate_export_header(_pyaccount
  BASE_NAME account
  )
