.. _python-bindings:


Mixing Python and compiled languages
====================================

.. questions::

   - Is there a way to automatically satisfy the dependencies of our code?

.. objectives::

   - Learn how to download your dependencies at configure-time with ``FetchContent``.
   - Learn how fetched content can be used natively within your build system.



Mixing C++ and Python with pybind11
+++++++++++++++++++++++++++++++++++

Python is an extremely flexible dynamic programming language. Since Python
itself is written in the C programming language, it is possible to write
*extension* modules in a compiled language. One gets all the flexibility, while
avoiding performance penalties inherent to interpreted languages.
Many frameworks are available to bridge the gap between compiled languages and
Python. All of them rely on some form of automatic code generation:

- `SWIG <http://swig.org/>`_. Possibly the framework with the longest history.
- `Cython <https://cython.org/>`_. Works with C and can require a lot of effort.
- `Boost.Python
  <https://www.boost.org/doc/libs/1_75_0/libs/python/doc/html/index.html>`_.
  Tailored for C++ and relies on template metaprogramming to generate bindings
  at compile-time.
- `pybind11 <https://pybind11.readthedocs.io/en/stable/index.html>`_. Same
  philosophy as Boost.Python, but designed for C++11 and beyond.

If you write modern C++, pybind11 should be your framework of choice:

- It is a header-only library and thus a rather easy dependency to satisfy.
- The binding code will be quite compact: you won't have to maintain an
  excessively large codebase.
- It has excellent integration with CMake.


.. exercise:: Banking code with C++ and Python

   Our goal is to compile Python wrappers to a small C++ library simulating a
   bank account. The pybind11 dependency will be satisfied at configure-time
   using ``FetchContent``.

   Get the :download:`scaffold code <code/tarballs/27_cxx-python.tar.bz2>`.
   The source tree is as follows:

   .. code-block:: text

      cxx-python
      └── account
          ├── account.cpp
          ├── account.hpp
          └── test.py

   #. Create a ``CMakeLists.txt`` in the root of the program, with minimum CMake requirement and project.
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

   You can download the :download:`complete, working example <code/tarballs/27_cxx-python_solution.tar.bz2>`.

   **Note** that:

   - The ``pybind11_add_module`` function is a convenience wrapper to
     |add_library| to generate Python extension modules. It is offered by
     pybind11 and you can read more about it `here
     <https://pybind11.readthedocs.io/en/stable/compiling.html#pybind11-add-module>`_.
   - The special syntax used in the definition of the test command will set
     the location of the Python extension as an environment variable.


.. warning::

   ``FetchContent`` is a powerful module in your CMake toolbox. **Beware!**
   Satisfying *every* dependency of your code in this way will make the duration
   of both the configuration and build stages balloon.



.. keypoints::

   - CMake lets you satisfy dependencies *on-the-fly*.
   - You can do so at build-time with ``ExternalProject``, but you need to adopt
     a superbuild framework.
   - At configure-time, you can use the ``FetchContent`` module: it can only be
     applied with dependencies that also use CMake.
