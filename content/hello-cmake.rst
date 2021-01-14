.. _hello-cmake:


From sources to executables
===========================

.. questions::

   - How do we use CMake to compile source files to executables?

.. objectives::

   - Learn what tools available in the CMake suite.
   - Learn how to write a simple ``CMakeLists.txt``.
   - Learn the difference between *build systems*, *build tools*, and *build system generator*.
   - Learn to distinguish between *configuration*, *generation*, and *build* time.
   - Learn how CMake structures build artifacts.


What is CMake?
--------------

Hello, CMake!
-------------

.. typealong:: Compiling "Hello, world" with CMake

   We will now proceed to compile a single source file to an executable. Choose
   your favorite language and start typing along!

   .. tabs::

      .. tab:: C++

         .. literalinclude:: code/solutions/hello-cxx/hello.cpp
            :language: c++

         You can download the :download:`complete, working example <code/solutions/hello-cxx/CMakeLists.txt>`

      .. tab:: Fortran

         .. literalinclude:: code/solutions/hello-f/hello.f90
            :language: fortran

         You can download the :download:`complete, working example <code/solutions/hello-f/CMakeLists.txt>`

   1. We will save our source file in a folder called ``hello``:

      .. code-block:: bash

         mkdir -p hello
         cd hello
   2.


The command-line interface to CMake
-----------------------------------


A complete toolchain
--------------------

.. figure:: img/cmake-times.jpg
   :align: center

   Depiction of the typemap for the ``Pair`` custom type. The displacements are
   always relative.


.. keypoints::

   - CMake is a **build system generator**, not a build system.
   - You write ``CMakeLists.txt`` to describe how the build tools will create artifacts from sources.
   - You can use the CMake suite of tools to manage the whole lifetime: from source files to tests to deployment.
   - The structure of the project is mirrored in the build folder.
