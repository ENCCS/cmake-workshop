.. _ctest-catch2:


C++ unit testing with Catch2
============================

.. questions::

   - How do we use CMake with a unit testing framework?

.. objectives::

   - Learn how to integrate the `Catch2 <https://github.com/catchorg/Catch2>`_ C++ unit test framework with CMake.


Unit testing is a valuable technique in software engineering: they can help
identify functional regression with a very fine level of control, since they are
meant to test isolated components in your codebase.
Equipping your codebase with integration *and* unit tests is very good practice.
There are many unit testing frameworks for the C++ language. Each of them
stresses a slightly different approach to unit testing and comes with its own
peculiarities in set up and usage.
In this episode, we will show how to use `Catch2
<https://github.com/catchorg/Catch2>`_ a very popular unit testing framework
which emphasizes a test-driven development workflow.
Catch2 is distributed as a single header file, which is one of its most
appealing features: it can easily be included in any project.


.. challenge::

   Get the :download:`scaffold code <code/tarballs/ctest-catch2.tar.bz2>`.

   1. Download the single header :download:`catch.hpp <https://github.com/catchorg/Catch2/releases/download/v2.13.4/catch.hpp>`
   2. Create a C++ project.
   3. Set the C++ standard to C++14. Catch2 will work with C++11 too.
   4. Create a library from the ``sum_integers.cpp`` source file.
   5. Link the library into a ``sum_up`` executable.
   6. Create the ``cpp_test`` executable.
   7. Enable testing and add a test. You will have to check how to call a Catch2
      executable.

   You can download the :download:`complete, working example <code/tarballs/ctest-labels_solution.tar.bz2>`.



.. keypoints::

   - It is rather straightforward to integrate Catch2 with a CMake-based build system.
   - Google Test is another popular C++ unit test framework, which is also well-integrated with  CMake.
