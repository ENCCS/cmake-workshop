.. _dependencies:


Finding and using dependencies
==============================

.. questions::

   - How can I use CMake to detect and use the dependencies of my project?

.. objectives::

   - Learn how to use |find_package|.
   - Learn what other detection alternatives exist.
   - Learn how to use the ``FetchContent`` module to retrieve dependencies at
     configure-time.

The vast majority of software projects do not happen in a vacuum: they will have
dependencies on existing frameworks and libraries.  Good documentation will
instruct your users to ensure that these are satisfied in their programming
environment. The build system is the appropriate place to check that these
preconditions are met and that your project can be built correctly.
In this episode, we will show you few examples of how to detect and use
dependencies in your CMake build system.

Finding dependencies
--------------------

CMake offers a family of commands to find artifacts installed on your system:

- |find_file| to retrieve the full path to a file.
- |find_library| to find a library, shared or static.
- |find_package| to find and load settings from an external project.
- |find_path| to find the directory containing a file.
- |find_program| to find an executable.

The workhorse of dependency discovery is |find_package|, which will cover your
needs in almost all use cases.

.. signature:: |find_package|

   .. code-block:: cmake

      find_package(<PackageName> [version] [EXACT] [QUIET] [MODULE]
             [REQUIRED] [[COMPONENTS] [components...]]
             [OPTIONAL_COMPONENTS components...]
             [NO_POLICY_SCOPE])

   This command will attempt finding the package with name ``<PackageName>`` by
   searching in a number of `predefined folders
   <https://cmake.org/cmake/help/latest/command/find_package.html?highlight=find_package#search-procedure>`_.
   It is possible to ask for a minimum or exact version. If ``REQUIRED`` is
   given, a failed search will trigger a fatal error.  The rules for the search
   are obtained from modules named ``Find<PackageName>.cmake``.
   Packages can also have *components* and you can ask to detect just a handful of them.


We cannot stress this enough: you should **only** use the other commands in the
``find_`` family in very special, very narrow circumstances.  Why so?

1. For a large selection of common dependencies, the ``Find<PackageName>.cmake``
   modules shipped with CMake work flawlessly and are maintained by the CMake
   developers. This lifts the burden of programming your own dependency
   detection tricks.
2. |find_package| will set up **imported targets**: targets defined *outside*
   your project that you can use with your own targets.  The properties on
   imported targets defines *usage requirements* for the dependencies. A command
   such as:

   .. code-block:: cmake

      target_link_libraries(your-target
        PUBLIC
          imported-target
        )

   will set compiler flags, definitions, include directories, and link libraries
   from ``imported-target`` to ``your-target`` *and* to all other targets in
   your project that will use ``your-target``.


These two points simplify **enormously** the burden of dependency detection and
consistent usage within a multi-folder project.


Using ``find_package``
++++++++++++++++++++++

When attempting dependency detection with |find_package|, you should make sure that:

- A ``Find<PackageName>.cmake`` module exists,
- Which components, if any, it provides, and
- What imported targets it will set up.

A complete list of ``Find<PackageName>.cmake`` can be found from the command-line interface:

.. code-block:: bash

   $ cmake --help-module-list | grep "Find"

.. typealong:: Using OpenMP

   We want to compile the following OpenMP sample code: [#omp]_

   .. code-block:: c++

      #include <cstdlib>

      void long_running_task(){
          // do something
      };

      void loop_body(int i, int j){
          // do something
      };

      void parallel_work() {
        int i, j;
      #pragma omp taskgroup
        {
      #pragma omp task
          long_running_task(); // can execute concurrently

      #pragma omp taskloop private(j) grainsize(500) nogroup
          for (i = 0; i < 10000; i++) { // can execute concurrently
            for (j = 0; j < i; j++) {
              loop_body(i, j);
            }
          }
        }
      }

      int main() {
        parallel_work();
        return EXIT_SUCCESS;
      }

   Note the usage of the ``taskloop`` construct, which was introduced in OpenMP
   4.5: we need to make sure our C++ compiler is suitably compatible with *at
   least* that version of the standard.

   From the documentation of the ``FindOpenMP.cmake`` module:

   .. code-block:: bash

      $ cmake --help-module FindOpenMP | less

   we find that the module provides the components ``C``, ``CXX``, and
   ``Fortran`` and that ``OpenMP::OpenMP_CXX`` target will be provided, if
   detection is successful.
   Thus, we do the following:

   .. code-block:: cmake

      find_package(OpenMP 4.5 REQUIRED COMPONENTS CXX)

      target_link_libraries(task-loop PRIVATE OpenMP::OpenMP_CXX)

   We can configure and build verbosely. #[verbose]_ Notice that compiler flags, include directories,
   and link libraries are properly resolved by CMake.

   You can download the :download:`complete working example <code/tarballs/taskloop_solution.tar.bz2>`.

.. challenge:: Using MPI

   In this exercise, you will attempt compiling a "Hello, world" program that
   uses the message passing interface (MPI).

   1. Check whether a ``FindMPI.cmake`` module exists in the built-in module library.
   2. Get acquainted with its components and the variables and imported targets it defines.

   .. tabs::

      .. tab:: C++

         Download the :download:`scaffold code <code/tarballs/mpi-cxx.tar.bz2>`.

         #. Compile the source file to an executable.
         #. Link against the MPI imported target.
         #. Invoke a verbose build and observe how CMake compiles and links.

         You can download the :download:`complete working example <code/tarballs/mpi-cxx_solution.tar.bz2>`.

      .. tab:: Fortran

         Download the :download:`scaffold code <code/tarballs/mpi-f.tar.bz2>`.

         #. Compile the source file to an executable.
         #. Link against the MPI imported target.
         #. Invoke a verbose build and observe how CMake compiles and links.

         You can download the :download:`complete working example <code/tarballs/mpi-f_solution.tar.bz2>`.


Alternatives: ``Config`` scripts and ``pkg-config``
+++++++++++++++++++++++++++++++++++++++++++++++++++

What to do when there is no built-in ``Find<PackageName>.cmake`` module for a package you depend on?
The package developers might be already prepared to help you out:

- They ship the CMake-specific file ``<PackageName>Config.cmake`` which
  describes how the imported target should be made for their package.
  In this case, you need to point CMake to the folder containing the ``Config`` file using the
  special ``<PackageName>_DIR`` variable:

  .. code-block:: bash

     $ cmake -S. -Bbuild -D<PackageName>_DIR=/folder/containing/<PackageName>Config.cmake

- They include a ``.pc`` file, which, on Unix-like platforms, can be detected
  with the ``pkg-config`` utility. You can then leverage ``pkg-config`` through CMake:

  .. code-block:: cmake

     # find pkg-config
     find_package(PkgConfig REQUIRED)
     # ask pkg-config to find the UUID library and prepare an imported target
     pkg_search_module(UUID REQUIRED uuid IMPORTED_TARGET)
     # use the imported target
     if(TARGET PkgConfig::UUID)
       message(STATUS "Found libuuid")
     endif()

  This was the strategy adopted in :ref:`probing` when testing the use of the
  UUID library.


Satisfying dependencies at configure-time
-----------------------------------------

CMake gives you the tools to satisfy missing dependencies at *configure-time*,
without user intervention. This is an extremely powerful mechanism, but you
should use it with care.

This is a built-in tool in CMake and will be made available by including the
``FetchContent`` module. There are two steps in this workflow:

#. *Declaring* the content to fetch with |FetchContent_Declare|. This can be a
   tarball (local or remote), a local folder, or a version control repository
   (Git, SVN, etc.).

   .. signature:: |FetchContent_Declare|

      .. code-block:: cmake

         FetchContent_Declare(<name> <contentOptions>...)

#. *Populating* the content with |FetchContent_MakeAvailable|. This commands
   *adds* the targets declared in the external content to your build system.

   .. signature:: |FetchContent_MakeAvailable|

      .. code-block:: cmake

         FetchContent_MakeAvailable( <name1> [<name2>...] )


.. challenge:: Catch2 reloaded

   In :ref:`ctest-catch2` we showed how to use the Catch2 testing framework and
   couple it with CTest.  We permanently added a copy of the ``catch.hpp``
   header file to the codebase. In this exercise, we want to download the header
   at configure-time, such that we don't store external code in our won
   repository.

   Before starting, get acquainted with the documentation
   for `declaring <https://cmake.org/cmake/help/latest/module/FetchContent.html#command:fetchcontent_declare>`_ and `making content available <https://cmake.org/cmake/help/latest/module/FetchContent.html#command:fetchcontent_makeavailable>`_.

   Get the :download:`scaffold code <code/tarballs/more-catch2.tar.bz2>`.

   #. Create a C++ project.
   #. Set the C++ standard to C++14. Catch2 will work with C++11 too.
   #. Create a library from the ``sum_integers.cpp`` source file.
   #. Link the library into a ``sum_up`` executable.
   #. Include the ``FetchContent`` module and declare the ``Catch2`` content. We
      want to download the ``v2.13.4`` tag from the `official Git repository <https://github.com/catchorg/Catch2>`_.
   #. Make the ``Catch2`` content available.
   #. Create the ``cpp_test`` executable.
   #. Enable testing and add a test. You will have to check how to call a Catch2
      executable.

   What differences do you note in the configuration step?

   You can download the :download:`complete, working example <code/tarballs/more-catch2_solution.tar.bz2>`.

.. warning::

   ``FetchContent`` is a powerful module in your CMake toolbox. **Beware!**
   Satisfying *every* dependency of your code in this way will make the duration
   of both the configuration and build stages balloon.


.. keypoints::

   - CMake has a rich ecosystem of modules for finding software dependencies. They are called ``Find<package>.cmake``.
   - The ``Find<package>.cmake`` modules are used through ``find_package(<package>)``.
   - You can also use the classic Unix tool ``pkg-config`` to find software
     dependencies, but this is not as robust as the CMake-native
     ``Find<package>`` modules.
   - You can also download dependencies at configure-time with the ``FetchContent`` module.



.. rubric:: Footnotes

.. [#omp]

   Example adapted from page 85 in `OpenMP 4.5 examples
   <http://www.openmp.org/wp-content/uploads/openmp-examples-4.5.0.pdf>`_.

.. [#verbose]

   The way in which to trigger a verbose build depends on the native build tool you are using.
   For Unix Makefiles:

   .. code-block:: bash

      $ cmake --build build -- VERBOSE=1

   For Ninja:

   .. code-block:: bash

      $ cmake --build build -- -v
