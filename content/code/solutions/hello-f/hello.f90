pure function say_hello() result(message)

  implicit none

  character(len=11) :: message

  message = 'Hello world'

end function

program hello_world

  implicit none

  character(len=11) :: say_hello

  print *, say_hello()

end program
