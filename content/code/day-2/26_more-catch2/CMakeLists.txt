# FIXME set minimum cmake version

# FIXME project name and language

# FIXME require C++14

# FIXME create sum_integers library

# FIXME create sum_up executable
# FIXME link sum_up executable to sum_integers library

# enable FetchContent
include(FetchContent)

# FIXME declare Catch2 content
FetchContent_Declare(...  # FIXME name of the content
  GIT_REPOSITORY ...  # FIXME the repository from which to download the content
  GIT_TAG        ...  # FIXME the tag to download
  )

# FIXME make content available
FetchContent_MakeAvailable(...)

# FIXME create cpp_test testing binary
# FIXME link cpp_test against the Catch2 imported target and the sum_integers library

# enable testing functionality
enable_testing()

# define test
add_test(
  NAME catch_test
  COMMAND $<TARGET_FILE:cpp_test> --success
  )
