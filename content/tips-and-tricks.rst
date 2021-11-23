.. _tips-and-tricks:

Porting your build system to CMake: tips and tricks
===================================================

.. objectives::

   - Learn what tools exist to structure projects as they grow.
   - Discuss the value of localizing scope and avoiding side effects.
   - Recognize more maintainable and less maintainable patterns.


As projects grow, things get more complicated: more possibilities, more corner
cases, more options to the user, and more developers who are contributing and
may not oversee the entire CMake structure. In this episode we will mention a
couple of tools to bring some structure and flow-control into larger projects.


Listing sources or globbing them
--------------------------------

In all our examples we have listed all sources when defining targets.

In CMake you can glob patters (e.g. all files that end with ``*.cpp``) without
listing them explicitly. This is tempting but do not do this. The reason is
that CMake cannot track dependency changes when you add files after you have
configured.

Listing files explicitly also allows to "grep" for them in the CMake code to
see where a modification is likely needed. This can help colleagues in our
projects who are not familiar with CMake to find out where to change things.


Options and flow control
------------------------

You may want to give the user the possibility to decide whether they want to
enable an option or not.

.. code-block:: cmake

   # by default this one will be ON
   option(ENABLE_MPI "Configure for MPI parallelization" ON)

   if(ENABLE_MPI)
     find_package(MPI REQUIRED COMPONENTS Fortran)
   else()
     message(STATUS "no problem, building without MPI")
   endif()

Now the user can decide:

.. code-block:: console

   $ cmake -S. -Bbuild -DENABLE_MPI=OFF


Organizing files into modules
-----------------------------

Modules are collections of functions and macros and are either CMake- or user-defined.
CMake comes with a rich ecosystem of modules and you will probably write a few
of your own to encapulate frequently used functions or macros in your CMake
scripts.

We have seen this module earlier today:

.. code-block:: cmake

   include(CMakePrintHelpers)

You can collect related CMake-code into a file called ``my_lengthy_code.cmake``
and then include it in another CMake code:

.. code-block:: cmake

   include(my_lengthy_code)

This can help organizing projects that are growing out of hand and separate
concerns.


Variables vs. targets
---------------------

In :ref:`targets` we have motivated why targets are preferable over variables.

When you portion your project into modules, then variable declaration impose an
order and the risk is high that somebody will not know about the implicit order
and reorder modules one day and the behavior will change.

Try to minimize the use of user-defined variables. They can point to a
sub-optimal solution and a better, more state-less, declarative, solution may
exist.


Functions and macros
--------------------

**Functions** and **macros** are build on top of the basic built-in commands
and are either CMake- or user-defined.  These prove useful to avoid repetition
in your CMake scripts.  The difference between a function and a macro is their
*scope*:

1. Functions have their own scope: variables defined inside a function are not
   propagated back to the caller.
2. Macros do not have their own scope: variables from the parent scope can be
   modified and new variables in the parent scope can be set.

Prefer functions over macros to minimize side-effects.


Where to list sources and tests?
--------------------------------

Some projects collect all sources in one file, all tests in another
file, and carry them across in variables:

.. code-block:: text

   project/
   ├── CMakeLists.txt
   ├── cmake
   |   ├── sources.cmake
   |   ├── tests.cmake
   |   └── definitions.cmake
   ├── external
   └── src
       ├── evolution
       ├── initial
       ├── io
       └── parser

Do this instead (sources, definitions, and tests defined in the "closest" ``CMakeLists.txt``):

.. code-block:: text

   project/
   ├── CMakeLists.txt
   ├── external
   │   ├── CMakeLists.txt
   └── src
       ├── CMakeLists.txt
       ├── evolution
       │   ├── CMakeLists.txt
       ├── initial
       │   ├── CMakeLists.txt
       ├── io
       │   ├── CMakeLists.txt
       └── parser
           └── CMakeLists.txt

The reason is that this will minimize side-effects, ordering effects, and
simplify maintenance for those who want to add or rename source files: they can
do it in one place, close to where they are coding.


Order and side effects
----------------------

When portioning your project into modules, design them in a way so that order
does not matter (much).

This is easier with functions than with macros and easier with targets than
with variables.

Avoid variables with parent or global scope. Encapsulate and prefer separation
of concerns.


Where to keep generated files
-----------------------------

CMake allows us to generate files at configure- or build-time.  When generating
files, always generate into the build folder, never outside the build folder.

The reason is that you always want to maintain the possibility to configure
different builds with the same source without having to copy the entire project
to a different place.
