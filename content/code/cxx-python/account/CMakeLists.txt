include(FetchContent)

FetchContent_Declare(pybind11
  URL https://github.com/pybind/pybind11/archive/v2.6.2.tar.gz
)

FetchContent_MakeAvailable(pybind11)

# use pybind11_add_module
pybind11_add_module(account)

# add sources
target_sources(account
  PRIVATE
    account.cpp
  )

# define test
add_test(
  NAME
    python_test
  COMMAND
    ${CMAKE_COMMAND} -E env ACCOUNT_MODULE_PATH=$<TARGET_FILE_DIR:account>
    ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test.py
  )
