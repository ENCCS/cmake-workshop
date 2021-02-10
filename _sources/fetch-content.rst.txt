.. _fetch-content:


Automated dependency handling with ``FetchContent``
===================================================

.. questions::

   - Is there a way to automatically satisfy the dependencies of our code?

.. objectives::

   - Learn how to download your dependencies at configure-time with ``FetchContent``.
   - Learn how fetched content can be used natively within your build system.


CMake offers **two modules** to satisfy missing dependencies on-the-fly:
the ``ExternalProject`` and ``FetchContent`` modules.

Using ``ExternalProject``
    - The download step happens at `project build-time
      <https://cmake.org/cmake/help/latest/module/ExternalProject.html>`_.
    - You can handle dependencies that **do not** use CMake.
    - You need to rewrite your whole build system as a `superbuild
      <https://github.com/dev-cafe/cmake-cookbook/blob/master/chapter-08/README.md>`_.
Using ``FetchContent``
    - The download step happens at `project configure-time
      <https://cmake.org/cmake/help/latest/module/FetchContent.html>`_.
    - You can only manage dependencies that use CMake.
    - It's an well-delimited change to an existing CMake build system.

Both are extremely powerful mechanisms, but you should use them with care.
Often, comprehensive documentation will suffice to help users set up their
environment to build your code successfully!  In this episode, we will discuss
the ``FetchContent`` module.


The ``FetchContent`` module
---------------------------

To fetch dependencies on-the-fly at configure-time you will include the built-in
CMake module ``FetchContent``.  This module has been part of CMake since its
3.11 version and has been steadily improved since then.

There are two steps in a ``FetchContent``-based workflow:

#. **Declaring** the content to fetch with |FetchContent_Declare|. This can be a
   tarball (local or remote), a local folder, or a version control repository
   (Git, SVN, etc.).

   .. signature:: |FetchContent_Declare|

      .. code-block:: cmake

         FetchContent_Declare(<name> <contentOptions>...)

      The command accepts as ``<contentOptions>`` the same options one would give
      to ``ExternalProject_Add`` in the *download* and *update/patch* `steps
      <https://cmake.org/cmake/help/latest/module/ExternalProject.html#command:externalproject_add>`_.

      To download code from a Git repository, you would set the following:

      - ``GIT_REPOSITORY``, the location of the repository.
      - ``GIT_TAG``, the revision (tag, branch name, commit hash) to check out.

      whereas to download a tarball you only need set:

      - ``URL``, the online location of the tarball.

#. **Populating** the content with |FetchContent_MakeAvailable|. This commands
   *adds* the targets declared in the external content to your build system.

   .. signature:: |FetchContent_MakeAvailable|

      .. code-block:: cmake

         FetchContent_MakeAvailable( <name1> [<name2>...] )

   Since targets from the external project are added to your own project, you
   will be able to use them in the same way you would when obtaining them
   through a call to |find_package|: you can use *found* and *fetched* content
   in the same exact way.
   If you need to set options for building the external project, you will set
   them as CMake variables *before* calling |FetchContent_MakeAvailable|.

Unit testing with Catch2
++++++++++++++++++++++++

Unit testing is a valuable technique in software engineering: it can help
identify functional regressions with a very fine level of control, since each
unit test is meant to exercise isolated components in your codebase.
Equipping your codebase with integration *and* unit tests is very good practice.

There are many unit testing frameworks for the C++ language. Each of them
stresses a slightly different approach to unit testing and comes with its own
peculiarities in set up and usage.
In this episode, we will show how to use `Catch2
<https://github.com/catchorg/Catch2>`_ a very popular unit testing framework
which emphasizes a test-driven development workflow.
Catch2 is distributed as a single header file, which is one of its most
appealing features: it can easily be included in any project. Rather than
download the header file and adding it to our codebase, we can use
``FetchContent`` to satisfy this dependency for us when needed.


.. challenge:: Catch2 reloaded

   We want to use the Catch2 unit testing framework for our code.  In this
   exercise, we will download the Catch2 project at configure-time from its
   `GitHub repository <https://github.com/catchorg/Catch2>`_.

   Get the :download:`scaffold code <code/tarballs/26_more-catch2.tar.bz2>`.

   #. Create a C++ project.
   #. Set the C++ standard to C++14. Catch2 will work with C++11 too.
   #. Create a library from the ``sum_integers.cpp`` source file.
   #. Link the library into a ``sum_up`` executable.
   #. Include the ``FetchContent`` module and declare the ``Catch2`` content. We
      want to download the ``v2.13.4`` tag from the `official Git repository <https://github.com/catchorg/Catch2>`_.
   #. Make the ``Catch2`` content available.
   #. Create the ``cpp_test`` executable.
   #. Enable testing and add a test. You will have to check how to call a Catch2
      executable in the `documentation
      <https://github.com/catchorg/Catch2/blob/v2.x/docs/command-line.md#specifying-which-tests-to-run>`_.
   #. Try running your tests.

   - What differences do you note in the configuration step?
   - What happens if you forget to issue the |FetchContent_MakeAvailable| command?
   - What targets are built in the project? Which ones are from Catch2? You can
     use the following command to obtain a list of all available targets:

     .. code-block:: bash

        $ cmake --build build --target help

   You can download the :download:`complete, working example <code/tarballs/26_more-catch2_solution.tar.bz2>`.

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


.. challenge:: Banking code with C++ and Python

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
