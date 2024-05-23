.. _cxx-fortran:


Mixing C++ and Fortran
======================

.. questions::

   - Can we use CMake to build mixed-language projects?

.. objectives::

   - Learn how the built-in ``FortranCInterface`` module can help you work with
     projects mixing Fortran and C/C++.


CMake has native support for many programming languages. At the time of writing,
C, C++, Fortran, CUDA, Objective-C, ISPC, and ASM are officially supported.
When programming applications and libraries in a scientific context, it is often
required to mix components written in different languages. This is mostly true
because legacy, tried-and-true components are extremely hard to replace by
non-professional programmers.
In this episode, we will show how to mix Fortran and C/C++.

In order to use multiple languages in your project, you can declare it within
the |project| command:

.. code-block:: cmake

   project(my-project LANGUAGES CXX Fortran)

Languages can also be declared later on in your ``CMakeLists.txt`` with
invocations to the ``enable_language`` command.
You can specify sources in multiple languages for any given executable or
library target. CMake will resolve which compiler to use for each based on their
extension: for example ``.f90`` will use the Fortran compiler, without
preprocessor.
Linking of mixed-language targets will be performed through the compiler of the
language with the highest priority. In C/Fortran projects, the Fortran compiler
will call the linker; in C++/Fortran projects, the C++ compiler will do the
honors.

The workhorse module for mixing C/C++ and Fortran is the built-in
``FortranCInterface`` module.  Whether you are working in Fortran and linking a
C/C++ library or viceversa, you should **always** check that the compilers for
the two languages are able to talk to each other.
That is where the |FortranCInterface_VERIFY| function comes into play:

.. code-block:: cmake

   include(FortranCInterface)

   # if you are working with C and Fortran
   FortranCInterface_VERIFY()

   # if you are working with C++ and Fortran
   FortranCInterface_VERIFY(CXX)


Fortran using C/C++
-------------------

If you are using Fortran2003 (and beyond), it is fairly straightforward to
employ C/C++ libraries. The ``iso_c_binding`` built-in module was indeed
mandated by the standards' committee starting from the 2003 edition, and
provides a standardized interface between C, the *de facto lingua franca* of
programming, and Fortran.
We will not delve into the details of ``iso_c_binding``,
suffice it so say that interoperability between basic datatypes, pointers, and
function call conventions is nowadays well-established. [#iso_c_binding]_

.. exercise:: Exercise 24: A Fortran executable using a C/C++ library

   In this exercise, you will build a Fortran executable linking to libraries
   written in C++ and the system library ``backtrace``, written in C.

   The final executable, ``bt-randomgen-example``, will print a few random
   integers, produced by the C++ library, and a backtrace, obtained from the C
   library. This is a sample output:

   .. code-block:: bash

      $ bt-randomgen-example

       Get a random number    20
       Get a random number    13
       Get a random number    30
       Get a random number    24
       Get a random number    40
       Get a random number    31
       Get a random number    33
       Get a random number    28
       Get a random number    33
       Get a random number    13
       Get a random number    11
       Get a random number    40
       Get a random number     7
       Get a random number    28
       Get a random number     5
       Get a random number    27
       Get a random number     4
       Get a random number    39
       Get a random number    38
       Get a random number    39
      Printing backtrace
      ./build/src/bt-randomgen-example[0x401316]
      ./build/src/bt-randomgen-example[0x401369]
      /nix/store/a3syww9igm49zdzq3ibzw9m8ccvsgxla-glibc-2.32/lib/libc.so.6(__libc_start_main+0xed)[0x7f87aa2b1dbd]
      ./build/src/bt-randomgen-example[0x40110a]

   The scaffold project is in ``content/code/day-2/24_fortran-cxx``.
   The project has the following source tree:

   .. code-block:: text

      fortran-cxx/
      └── src
          ├── bt-randomgen-example.f90
          ├── interfaces
          │   ├── interface_backtrace.f90
          │   ├── interface_randomgen.f90
          │   └── randomgen.cpp
          └── utils
              └── util_strings.f90

   #. Add ``CMakeLists.txt`` files where necessary. You can either declare
      Fortran, C++, and C as project languages, or enable C++ and C in the
      ``interfaces`` folder.
   #. In the ``src`` folder, create an executable from the
      ``bt-randomgen-example.f90`` file. This executable will have to be linked
      to the libraries created in the ``utils`` and ``interfaces`` folders.
   #. Modify the scaffold ``CMakeLists.txt`` in the ``interfaces`` folder to
      build a shared library from the C++ and Fortran sources. **Beware**, for
      CMake to resolve Fortran modules dependencies, you need to specify the
      corresponding sources with ``PUBLIC`` visibility level.
   #. Do not forget to verify that the C/C++ and Fortran compilers are compatible!
   #. Try out the executable and **remember** that the build tree *mirrors* the source tree.

   A working solution is in the ``solution`` subfolder.


C/C++ using Fortran
-------------------

Whenever a mix of C/C++ and Fortran is necessary, one needs to be aware of some
fundamental differences between the languages:

- Fortran arrays are column-major.
- All function arguments are passed by-reference.
- Fortran compilers *mangle* function names. Usually by adding an underscore at the end.
- Fortran is case-insensitive.

Fortran90 introduced a number of modern features: *modules*, *function
overloading*, and *user-defined types*. These features further complicate
interoperability: they require compilers to perform more extensive `name
mangling <https://en.wikipedia.org/wiki/Name_mangling>`_. As the mangling is not
standard-mandated, each vendor can decide how to perform it.

The ``FortranCInterface`` module fortunately comes to the rescue! The function
|FortranCInterface_HEADER| will generate a header file with all the macros
needed to mangle names as appropriate for the compiler in use:

.. signature:: |FortranCInterface_HEADER|

   .. code-block:: cmake

      FortranCInterface_HEADER(<file>
                         [MACRO_NAMESPACE <macro-ns>]
                         [SYMBOL_NAMESPACE <ns>]
                         [SYMBOLS [<module>:]<function> ...])


.. parameters::

   ``<file>``
       Name of the header file with name mangling macros:

       .. code:: c

          #define FortranCInterface_GLOBAL (name,NAME) ...
          #define FortranCInterface_GLOBAL_(name,NAME) ...
          #define FortranCInterface_MODULE (mod,name, MOD,NAME) ...
          #define FortranCInterface_MODULE_(mod,name, MOD,NAME) ...

       These can be used for global (module) symbols. Use the macros ending with
       an underscore to mangle symbols containing underscores.
   ``MACRO_NAMESPACE``
       Optional, to replace the default ``FortranCInterface_`` prefix with a
       given namespace ``<macro-ns>``.
   ``SYMBOLS``
       Optional, list of symbols to mangle automatically with C preprocessor
       definitions.
   ``SYMBOL_NAMESPACE``
       Optional, prefix all preprocessor definitions generated by the
       ``SYMBOLS`` option with a given namespace ``<ns>``.


.. exercise:: Exercise 25: A C/C++ executable using a Fortran library

   Your goal is to link a C++ executable to a BLAS/LAPACK library.  The final
   executable will be named ``linear-algebra``: it scales a vector with
   ``DSCAL`` and performs a linear solve with ``DGESV``.  We assume the
   BLAS/LAPACK library to be written in Fortran.  This means that the symbols
   for ``DSCAL`` and ``DGESV`` are mangled in a compiler-dependent way.
   The ``linear-algebra`` executable will accept the dimension of the square
   matrix and vector as command-line input, for example:

   .. code-block:: bash

      $ linear-algebra 1000

      C_DSCAL done
      C_DGESV done
      info is 0
      check is 4.80085e-12

   The scaffold project is in ``content/code/day-2/25_cxx-fortran``.
   The project has the following source tree:

   .. code-block:: text

      cxx-fortran/
      ├── README.md
      └── src
          ├── linear-algebra.cpp
          └── math
              ├── CxxBLAS.cpp
              ├── CxxBLAS.hpp
              ├── CxxLAPACK.cpp
              └── CxxLAPACK.hpp

   #. Inspect the contents of the C++ sources in the ``math`` subfolder. They
      refer to a ``fc_mangle.h`` header file, which is not part of the project,
      as it will be automatically generated.
   #. Create an executable from the ``linear-algebra.cpp`` source file.
   #. Complete the scaffold ``CMakeLists.txt`` in the ``math`` subfolder. In
      particular, you want to check compatibility of compilers and generate the
      ``fc_mangle.h`` header. Hint: you will have to use the
      ``SYMBOLS`` option to the |FortranCInterface_HEADER|.
   #. Try out the executable and **remember** that the build tree *mirrors* the source tree.

   A working solution is in the ``solution`` subfolder.


.. keypoints::

   - Always check whether the Fortran and C/C++ compilers you are using are
     interoperable.
   - Fortran name-mangling header files for C/C++ can be conveniently
     autogenerated by CMake.


.. rubric:: Footnotes

.. [#iso_c_binding]

   You can find out more about ``iso_c_binding`` and Fortran/C interoperability
   in the `GNU Fortran manual
   <https://gcc.gnu.org/onlinedocs/gfortran/Interoperability-with-C.html>`_.
