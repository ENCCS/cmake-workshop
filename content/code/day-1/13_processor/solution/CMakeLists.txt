# set minimum cmake version
cmake_minimum_required(VERSION 3.18)

# project name and language
project(processor LANGUAGES NONE)

# the value of NUMBER_OF_LOGICAL_CORES will be saved in _NUMBER_OF_LOGICAL_CORES
cmake_host_system_information(RESULT _NUMBER_OF_LOGICAL_CORES QUERY NUMBER_OF_LOGICAL_CORES)
message(STATUS "Number of logical cores : ${_NUMBER_OF_LOGICAL_CORES}")
