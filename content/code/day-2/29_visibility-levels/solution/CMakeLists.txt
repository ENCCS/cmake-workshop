# define minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and supported language
project(bank LANGUAGES CXX)

# require C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# interface and sources
add_subdirectory(account)

add_executable(bank bank.cpp)

target_link_libraries(bank
  PRIVATE
    account
  )
