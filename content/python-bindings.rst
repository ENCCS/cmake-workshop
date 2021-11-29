.. _python-bindings:


Mixing Python and compiled languages
====================================

.. questions::

   - Is there a way to automatically satisfy the dependencies of our code?

.. objectives::

   - Learn how to download your dependencies at configure-time with ``FetchContent``.
   - Learn how fetched content can be used natively within your build system.


Python is a flexible dynamic programming language. Since Python
itself is written in the C programming language, it is possible to write
*extension* modules in a compiled language. One gets all the flexibility, while
avoiding performance penalties inherent to interpreted languages.
Many frameworks are available to bridge the gap between compiled languages and
Python. All of them rely on some form of automatic code generation:

- `SWIG <http://swig.org/>`_. Possibly the framework with the longest history.
- `CFFI <https://cffi.readthedocs.io/en/latest/index.html>`_. Works with C and
  Fortran.
- `Cython <https://cython.org/>`_. Works with C and can require a lot of effort.

Mixing C++ and Python with pybind11
+++++++++++++++++++++++++++++++++++

If you are writing C++, you have even more choice of binding frameworks:

- `Boost.Python
  <https://www.boost.org/doc/libs/1_75_0/libs/python/doc/html/index.html>`_.
  Tailored for C++ and relies on template metaprogramming to generate bindings
  at compile-time.
- `pybind11 <https://pybind11.readthedocs.io/en/stable/index.html>`_. Same
  philosophy as Boost.Python, but designed for C++11 and beyond.

If you write *modern C++*, pybind11 should be your framework of choice:

- It is a header-only library and thus a rather easy dependency to satisfy.
- The binding code will be quite compact: you won't have to maintain an
  excessively large codebase.
- It has excellent integration with CMake.


.. exercise:: Exercise 27: Banking code with C++ and Python

   Our goal is to compile Python wrappers to a small C++ library simulating a
   bank account. The pybind11 dependency will be satisfied at configure-time
   using ``FetchContent``.

   A scaffold for the project is in ``content/code/day-2/27_cxx-pybind11``.
   The source tree is as follows:

   .. code-block:: text

      27_cxx-pybind11
      └── account
          ├── account.cpp
          ├── account.hpp
          └── test.py

   #. Create a ``CMakeLists.txt`` in the root of the program, with minimum CMake
      requirement and project.
   #. Find the Python with |find_package|. Request at least version 3.6 with the
      ``REQUIRED`` keyword and the interpreter and development headers with the
      ``COMPONENTS`` keyword. Refer to the documentation:

      .. code-block:: bash

         $ cmake --help-module FindPython | less

   #. Enable testing and add the ``account`` folder.
   #. Complete the scaffold ``CMakeLists.txt`` in the ``account`` folder,
      following the ``FIXME`` prompts. We want to download the released tarball
      for version 2.6.2 of pybind11.
   #. Configure, build, and run the test.

   A working solution is in the ``solution`` subfolder.

   .. note::

      - The ``pybind11_add_module`` function is a convenience wrapper to
        |add_library| to generate Python extension modules. It is offered by
        pybind11 and you can read more about it `here
        <https://pybind11.readthedocs.io/en/stable/compiling.html#pybind11-add-module>`_.
      - The special syntax used in the definition of the test command will set
        the location of the Python extension as an environment variable.


Mixing C/Fortran and Python with CFFI
+++++++++++++++++++++++++++++++++++++

`CFFI <https://cffi.readthedocs.io/en/latest/index.html>`_, short for "C Foreign
Function Interface", is a Python module that helps with creating Python
interfaces for C-interoperable projects.
Using CFFI can be slightly more low-level than working with pybind11. However,
it allows you to create Python interfaces for Fortran projects more
straightforwardly than with Cython or SWIG.




.. exercise:: Exercise 28: Banking code using CFFI

   Our goal is to compile Python wrappers to a small library simulating a
   bank account.

   .. tabs::

      .. tab:: C++

         A scaffold for the project is in ``content/code/day-2/28_cxx-cffi``.
         The source tree is as follows:

         .. code-block:: text

            28_cxx-cffi
            └── account
                ├── account.cpp
                ├── account.hpp
                └── test.py

         #. Create a ``CMakeLists.txt`` in the root of the program, with minimum
            CMake requirement and project.
         #. Find the Python with |find_package|. Request at least version 3.6 with the
            ``REQUIRED`` keyword and the interpreter and development headers with the
            ``COMPONENTS`` keyword. Refer to the documentation:

            .. code-block:: bash

               $ cmake --help-module FindPython | less

         #. Enable testing and add the ``account`` folder.
         #. Complete the scaffold ``CMakeLists.txt`` in the ``account`` folder,
            following the ``FIXME`` prompts. We want to download the released tarball
            for version 2.6.2 of pybind11.
         #. Configure, build, and run the test.

         A working solution is in the ``solution`` subfolder.

      .. tab:: Fortran

         A scaffold for the project is in ``content/code/day-2/28_fortran-cffi``.
         The source tree is as follows:

         .. code-block:: text

            28_fortran-cffi
            └── account
                ├── account.cpp
                ├── account.hpp
                └── test.py

         #. Create a ``CMakeLists.txt`` in the root of the program, with minimum
            CMake requirement and project.
         #. Find the Python with |find_package|. Request at least version 3.6 with the
            ``REQUIRED`` keyword and the interpreter and development headers with the
            ``COMPONENTS`` keyword. Refer to the documentation:

            .. code-block:: bash

               $ cmake --help-module FindPython | less

         #. Enable testing and add the ``account`` folder.
         #. Complete the scaffold ``CMakeLists.txt`` in the ``account`` folder,
            following the ``FIXME`` prompts. We want to download the released tarball
            for version 2.6.2 of pybind11.
         #. Configure, build, and run the test.

         A working solution is in the ``solution`` subfolder.



.. keypoints::

   - CMake lets you satisfy dependencies *on-the-fly*.
   - You can do so at build-time with ``ExternalProject``, but you need to adopt
     a superbuild framework.
   - At configure-time, you can use the ``FetchContent`` module: it can only be
     applied with dependencies that also use CMake.
