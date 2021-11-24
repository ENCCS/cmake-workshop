cmake_minimum_required(VERSION 3.18)

project(check_compiler_flag LANGUAGES CXX)

# we set the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# add an executable target
add_executable(asan-example asan-example.cpp)

# we set some generic compiler flags
target_compile_options(asan-example
  PUBLIC
    "-g3"
    "-O1"
  )

include(CheckCXXCompilerFlag)

set(ASAN_FLAGS "-fsanitize=address -fno-omit-frame-pointer")

set(CMAKE_REQUIRED_FLAGS ${ASAN_FLAGS})
check_cxx_compiler_flag(${ASAN_FLAGS} asan_works)
unset(CMAKE_REQUIRED_FLAGS)

if(asan_works)
  # we transform ASAN_FLAGS to ;-separated list
  string(REPLACE " " ";" _asan_flags ${ASAN_FLAGS})
  target_compile_options(asan-example
    PUBLIC
      ${_asan_flags}
    )
  # this is needed for the linker to properly handle the sanitizer
  target_link_libraries(asan-example
    PUBLIC
      ${_asan_flags}
    )
endif()
