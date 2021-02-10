.. _hello-ctest:


Creating and running tests with CTest
=====================================

.. questions::

   - How can we handle the testing stage of our project with CMake?

.. objectives::

   - Learn how to produce test executables with CMake.
   - Learn how to run your tests through CTest.


Testing is an essential activity in the development cycle. A well-designed test
suite will help you detect bugs and can also facilitate the onboarding of new
developers.
In this episode, we will look into how to use CTest to define and run our tests.

Adding tests to your project
----------------------------

In CMake and CTest, a test is any command returning an exit code. It does not
really matter how the command is issued or what is run: it can be a C++
executable or a Python script. As long as the execution returns a zero or
non-zero exit code, CMake will be able to classify the test as succeeded or
failed, respectively.

There are two steps to perform to integrate your CMake build system with the CTest tool:

1. Call the ``enable_testing`` command. This takes no arguments.
2. Add tests with the |add_test| command.

.. signature:: |add_test|

   .. code-block:: cmake

      add_test(NAME <name> COMMAND <command> [<arg>...]
         [CONFIGURATIONS <config>...]
         [WORKING_DIRECTORY <dir>]
         [COMMAND_EXPAND_LISTS])

   This command accepts *named arguments*, only ``NAME`` and ``COMMAND`` are
   mandatory.  The former specifies the identifying name of the test, while the
   latter sets up what command to run.


.. typealong:: Your first test project

   We will build a simple library to sum integers and an executable using this library.
   We will work from a :download:`scaffold project <code/tarballs/05_hello-ctest.tar.bz2>`.

   .. code-block:: cmake

      cmake_minimum_required(VERSION 3.13)

      project(hello-ctest LANGUAGES CXX)

      set(CMAKE_CXX_STANDARD 14)
      set(CMAKE_CXX_EXTENSIONS OFF)
      set(CMAKE_CXX_STANDARD_REQUIRED ON)

      add_library(sum_integers sum_integers.cpp)

      add_executable(sum_up main.cpp)
      target_link_libraries(sum_up PRIVATE sum_integers)

   Alongside the library and the main executable, we will also produce an
   executable to test the ``sum_integers`` library.

   .. code-block:: cmake

      add_executable(cpp_test test.cpp)
      target_link_libraries(cpp_test PRIVATE sum_integers)

   It is now time to set up CTest:

   .. code-block:: cmake

      enable_testing()

   and declare our test, by specifying which command to run:

   .. code-block:: cmake

      add_test(
        NAME cpp_test
        COMMAND $<TARGET_FILE:cpp_test>
      )

   Note the use of `generator expression (gen-exp)
   <https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html>`_
   to avoid specifying the complete path to the executable ``cpp_test``.

   We can now compile and run our test:

   .. code-block:: bash

      $ cmake -S. -Bbuild
      $ cd build
      $ cmake --build .
      $ ctest

   You can download the :download:`complete, working example <code/tarballs/05_hello-ctest.tar.bz2>`.

.. challenge:: Running the tests through a shell script

   Any command can be used to run tests. In this exercise, we will extend the
   previous CMake code to test the main executable within a shell script.

   1. Get the :download:`scaffold code <code/tarballs/06_bash-ctest.tar.bz2>`.
   2. Find the appropriate bash executable to run ``test.sh`` with. You should
      use the ``find_program`` command of CMake.
   3. Add another invocation to |add_test| that will be equivalent to running:

      .. code-block:: bash

         $ ./test.sh sum_up

   4. Build the project and run CTest.

   You can download the :download:`complete, working example <code/tarballs/06_bash-ctest_solution.tar.bz2>`.

.. challenge:: Running the tests through a Python script

   It is much more common nowadays to use Python, rather than shell scripts.  In
   this exercise, we will add two more tests to our project. These new tests
   will run the main executable through a Python script.

   #. Get the :download:`scaffold code <code/tarballs/07_python-ctest.tar.bz2>`.
   #. Find the Python interpreter to run ``test.py``. You should
      use the |find_package| command of CMake.
   #. Add another invocation to |add_test| that will be equivalent to running:

      .. code-block:: bash

         $ python test.py --executable sum_up

   #. The ``test.py`` script accepts a ``--short`` command-line option. Add
      another test that uses this option in the command.
   #. Build the project and run CTest.

   You can download the :download:`complete, working example <code/tarballs/07_python-ctest_solution.tar.bz2>`.

The CTest command-line interface
--------------------------------

.. typealong:: How to use CTest effectively.

   We will now demonstrate the CTest command-line interface (CLI) using the
   solution of the previous exercise.

   The ``ctest`` command is part of the CMake installation. We can find help on its usage with:

   .. code-block:: bash

      $ ctest --help

   **Remember**, to run your tests through CTest, you will first need to move
   into the build folder:

   .. code-block:: bash

      $ cd build
      $ ctest

   This will run all the tests in your test suite.
   You can list the names of the tests in the test suite with:

   .. code-block:: bash

      $ ctest -N

   Verbosity options are also quite helpful, especially when debugging failures.
   With ``--output-on-failure``, CTest will print to screen the output of
   failing tests.
   If you would like to print to screen the full invocation for every test, use
   the ``--verbose`` option.
   You can select *subsets* of test to run:

   - By *name*, with the ``-R <regex>`` flag. Any test whose *name* can be
     captured by the passed regex will be run.  The ``-RE <regex>`` option
     *excludes* tests by name using a regex.
   - By *label*, with the ``-L <regex>`` flag. Any test whose *labels* can be
     captured by the passed regex will be run.  The ``-LE <regex>`` option
     *excludes* tests by label using a regex.
   - By *number*, with the ``-I [Start,End,Stride,test#,test#|Test file]`` flag.
     This is usually not the most convenient option for selecting subsets of
     tests.

   It is possible to rerun failed tests with:

   .. code-block:: bash

      $ ctest --rerun-failed

   Finally, you can parallelize test execution:

   .. code-block:: bash

      $ ctest -j N
      $ ctest --parallel N

   **Beware!** The order of execution of tests is not guaranteed: if some tests
   are interdependent, you will have to explicitly state that in your build
   system.


Test properties: labels, timeout, and cost
------------------------------------------

When you use |add_test|, you give a unique name to each test. As we have seen,
you can use these names to filter which tests to run in the suite. This can be
extremely valuable when the test suite is large and you really only need to run
few of the many tests.
However, the naming mechanism does not allow to easily group tests. We could in
principle add a suffix to all tests in a given group and then filter them with
an appropriate regex, but what if we had multiple groups to which tests could
belong. This is a very common situation in practice!
Fortunately, we can set **properties** on tests and labels are among the
available properties.

.. signature:: |set_tests_properties|

   .. code-block:: cmake

      set_tests_properties(test1 [test2...] PROPERTIES prop1 value1 prop2 value2)


.. challenge:: Set labels on tests

   We will run some tests using Python and we want to group them into two categories:

   - ``quick`` for tests with a very short execution time.
   - ``long`` for benchmarking tests with a longer execution time.

   Get the :download:`scaffold code <code/tarballs/08_ctest-labels.tar.bz2>`.

   .. tabs::

      .. tab:: Labeling

         1. Find the Python interpreter.
         2. Enable testing.
         3. Add the six tests in the ``test`` folder. Give each of them a unique name.
         4. Use |set_tests_properties| to set labels for the tests:

            - ``feature-a.py``, ``feature-b.py``, and ``feature-c.py`` should be
              in the ``quick`` group.
            - ``feature-d.py``, ``benchmark-a.py``, and ``benchmark-b.py``
              should be in the ``long`` group.

         5. Check that everything works as expected

      .. tab:: Bonus

         Try simplifying the repeated calls to |add_test| with a |foreach| loop.
         You might need to apply some filename manipulations: check out the
         ``file`` command.

   You can download the :download:`complete, working example <code/tarballs/08_ctest-labels_solution.tar.bz2>`.
   

Among the many properties that can be set on tests, we would like to highlight the following:

- ``WILL_FAIL``. CTest will mark tests as passed when the corresponding command
  returns with a non-zero exit code. Use this property to test for expected
  failures.
- ``COST``. The first time you run your tests, CTest will save the run time of
  each. In this way, subsequent runs of the test suite will start by executing
  the longest running tests first. You can influence this behavior by declaring
  up front the "cost" of each test.
- ``TIMEOUT``. Some tests might run for a long time: you can set an explicit
  timeout if you want to be more or less tolerant of variations in execution
  time.

.. challenge:: More properties!

   Let's play around with the properties we have just introduced.

   .. tabs::

      .. tab:: WILL_FAIL

         Get the :download:`scaffold code <code/tarballs/09_ctest-will-fail.tar.bz2>`.

         1. Create a project with no language.
         2. Find the Python interpreter.
         3. Enable testing.
         4. Add a test running the ``test.py`` script.

         Try to run the tests and observe what happens.  Now set the
         ``WILL_FAIL`` property to true and observe what changes when running
         the tests.

         You can download the :download:`complete, working example <code/tarballs/09_ctest-will-fail_solution.tar.bz2>`.

      .. tab:: COST

         Get the :download:`scaffold code <code/tarballs/10_ctest-cost.tar.bz2>`.

         1. Enable testing in the ``CMakeLists.txt`` file.
         2. Add tests running each of the scripts in the ``test`` folder.
         3. Run the tests in parallel and observe how long their execution takes.
         4. Re-run the tests and observe how CTest orders their execution.
         5. Now set the ``COST`` property. What has changed when re-running the tests.

         You can download the :download:`complete, working example <code/tarballs/10_ctest-cost_solution.tar.bz2>`.

      .. tab:: TIMEOUT

         Get the :download:`scaffold code <code/tarballs/11_ctest-timeout.tar.bz2>`.

         1. Create a project with no language.
         2. Find the Python interpreter.
         3. Enable testing.
         4. Add a test running the ``test.py`` script.

         Try to run the tests and observe how long the test takes to execute.
         Now set the ``TIMEOUT`` property to a value *less* than what you just
         observed and re-run the tests.

         You can download the :download:`complete, working example <code/tarballs/11_ctest-timeout_solution.tar.bz2>`.


For a complete list of properties that can be set on tests search for
"Properties on Tests" in the output of:

.. code-block:: bash

   $ cmake --help-properties

or visit the CMake documentation `online <https://cmake.org/cmake/help/v3.19/manual/cmake-properties.7.html#properties-on-tests>`_.



.. keypoints::

   - Any custom command can be defined as a test in CMake.
   - Tests can be run through CTest.
