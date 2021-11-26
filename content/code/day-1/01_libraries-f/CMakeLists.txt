# FIXME set minimum cmake version
cmake_minimum_required(...)

# FIXME declare project giving project name and language
project(... LANGUAGES ...)

# FIXME create the message library from the message.f90 source file
add_library(...)

# FIXME create hello-world executable from hello-world.f90
add_executable(hello-world ...)

# FIXME link hello-world to the message library
target_link_libraries(hello-world ...)
