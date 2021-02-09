add_library(evolution)

target_sources(evolution
  PRIVATE
    empty.f90
  PUBLIC
    ancestors.f90
    evolution.f90
  )
