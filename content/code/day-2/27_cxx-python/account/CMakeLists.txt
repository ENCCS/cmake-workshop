# FIXME enable FetchContent
include(...)

# FIXME declare and make available pybind11 external content
FetchContent_Declare(...)

# use pybind11_add_module
pybind11_add_module(account)

# FIXME add sources to  account target
target_sources(account
  ...
  )

# define test
add_test(
  NAME
    python_test
  COMMAND
    ${CMAKE_COMMAND} -E env ACCOUNT_MODULE_PATH=$<TARGET_FILE_DIR:account>
    ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test.py
  )
