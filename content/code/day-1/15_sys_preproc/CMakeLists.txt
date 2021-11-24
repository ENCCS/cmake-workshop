# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(sys_preproc LANGUAGES CXX)

# define executable and its source file
add_executable(hello-world hello-world.cpp)

# let the preprocessor know about the system name
if(CMAKE_SYSTEM_NAME ...)
  # add IS_LINUX definition
  target_compile_definitions(...)
endif()
if(CMAKE_SYSTEM_NAME ...)
  # add IS_MACOS definition
  target_compile_definitions(...)
endif()
if(CMAKE_SYSTEM_NAME ...)
  # add IS_WINDOWS definition
  target_compile_definitions(...)
endif()
