cmake_minimum_required(VERSION 3.18)

project(taskloop LANGUAGES CXX)

add_executable(taskloop taskloop.cpp)

find_package(OpenMP 4.5 REQUIRED COMPONENTS CXX)

target_link_libraries(taskloop PRIVATE OpenMP::OpenMP_CXX)
