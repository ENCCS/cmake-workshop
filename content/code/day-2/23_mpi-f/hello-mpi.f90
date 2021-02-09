program main

  use mpi

  integer ( kind = 4 ) error
  integer ( kind = 4 ) id
  integer ( kind = 4 ) p
!
!  Initialize MPI.
!
  call MPI_Init ( error )
!
!  Get the number of processes.
!
  call MPI_Comm_size ( MPI_COMM_WORLD, p, error )
!
!  Get the individual process ID.
!
  call MPI_Comm_rank ( MPI_COMM_WORLD, id, error )
!
!  Every MPI process will print this message.
!
  write ( *, '(a,i1,2x,a)' ) 'P', id, '"Hello, world!"'
!
!  Shut down MPI.
!
  call MPI_Finalize ( error )
end program
