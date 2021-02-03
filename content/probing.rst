.. _probing:


Probing compilation, linking, and execution
===========================================

.. questions::

   - How can you add custom steps to your build system with CMake?

.. objectives::

   - Learn how and when to use ``execute_process``
   - Learn how to use ``add_custom_command`` with targets.
   - Learn how to test compilation, linking, and execution.


Running custom commands at *configure-time*
-------------------------------------------

.. todo::

   - Pitfalls of |execute_process|


.. signature:: |execute_process|

   .. code-block:: cmake

      execute_process(COMMAND <cmd1> [args1...]]
                      [COMMAND <cmd2> [args2...] [...]]
                      [WORKING_DIRECTORY <directory>]
                      [TIMEOUT <seconds>]
                      [RESULT_VARIABLE <variable>]
                      [RESULTS_VARIABLE <variable>]
                      [OUTPUT_VARIABLE <variable>]
                      [ERROR_VARIABLE <variable>]
                      [INPUT_FILE <file>]
                      [OUTPUT_FILE <file>]
                      [ERROR_FILE <file>]
                      [OUTPUT_QUIET]
                      [ERROR_QUIET]
                      [OUTPUT_STRIP_TRAILING_WHITESPACE]
                      [ERROR_STRIP_TRAILING_WHITESPACE]
                      [ENCODING <name>])

   Executes one or more child processes.  The standard output and standard error
   streams are recorded into ``OUTPUT_VARIABLE`` and ``ERROR_VARIABLE``,
   respetively. The result of the last child process is saved into
   ``RESULT_VARIABLE``.


.. challenge:: Find a Python module

   In this exercise, we'll use |execute_process| to check whether the `cffi
   <https://cffi.readthedocs.io/en/latest/index.html>`_ Python module is
   installed in your environment. On the command line, you would do:

   .. code-block:: bash

      $ python -c "import cffi; print(cffi.__version__)"

   Your goal is to replicate the same in CMake.

   1. Get the :download:`scaffold code <code/tarballs/find_cffi.tar.bz2>`.
   2. Modify the call to |execute_process| to run the command above.

   Note the use of ``find_package(Python REQUIRED)`` to obtain the ``python``
   executable. We will revisit uses of |find_package| later on in
   :ref:`dependencies`.

   You can download the :download:`complete, working example <code/tarballs/find_cffi_solution.tar.bz2>`.

Custom commands for your targets
--------------------------------

.. todo::

   - |add_custom_command| with ``PRE_LINK`` and ``POST_BUILD``


.. signature:: |add_custom_command|

   .. code-block:: cmake

      add_custom_command(TARGET <target>
                   PRE_BUILD | PRE_LINK | POST_BUILD
                   COMMAND command1 [ARGS] [args1...]
                   [COMMAND command2 [ARGS] [args2...] ...]
                   [BYPRODUCTS [files...]]
                   [WORKING_DIRECTORY dir]
                   [COMMENT comment]
                   [VERBATIM] [USES_TERMINAL])

   Add one or more custom commands to a target, such as a library or an
   executable.  The commands can be executed before linking (with ``PRE_BUILD``
   and ``PRE_LINK``) or after (with ``POST_BUILD``)


.. challenge:: Before and after build

   We want to perform some action before and after building a target, in this case a Fortran executable:

   - Before building, we want to read the link line, as produced by CMake, and
     echo it to standard output. We use the ``echo.py`` Python script.
   - After building, we want to check the size of the static allocations in the
     binary, by invoking the ``size`` command. We use the ``static-size.py`` Python script.

   1. Get the :download:`scaffold code <code/tarballs/pre_post.tar.bz2>`.
   2. Add CMake commands to build the ``example`` executable from the Fortran
      sources.  Find the text file with the link line under the build folder.
      Hint: have a look in ``CMakeFiles`` and keep in mind the name you gave to
      the target.
   3. Call |add_custom_command| with ``PRE_LINK`` to invoke the ``echo.py`` Python script.
   4. Call |add_custom_command| with ``POST_BUILD`` to invoke the ``static-size.py`` Python script.

   You can download the :download:`complete, working example <code/tarballs/pre_post_solution.tar.bz2>`.


Testing compilation, linking, and execution
-------------------------------------------


.. todo::

   - |try_compile| and pitfalls
   - |check_<lang>_compiler_flag|
   - |check_<lang>_source_runs|


.. challenge:: Check that a compiler accepts a compiler flag

   Compilers evolve: they add and/or remove flags and sometimes you will face
   the need to test whether some flags are available before using them in your
   build.

   1. Get the :download:`scaffold code <code/tarballs/check_compiler_flag.tar.bz2>`.
   2. Implement a ``CMakeLists.txt`` to build an executable from the
      ``asan-example.cpp`` source file.
   3. Check that the address sanitizer flags are available with
      |check_cxx_compiler_flag|. The flags to check are ``-fsanitize=address
      -fno-omit-frame-pointer``.
   4. If the flags do work, add them to the those used to compile the executable
      target with |target_compile_options|.

   You can download the :download:`complete, working example <code/tarballs/check_compiler_flag_solution.tar.bz2>`.


.. challenge:: Testing runtime capabilities

   Testing that some features will work properly for your code requires not only
   compiling an object files, but also linking an executable and running it
   successfully.

   1. Get the :download:`scaffold code <code/tarballs/check_source_runs.tar.bz2>`.
   2. Create an executable target from the source file ``use-uuid.cpp``.
   3. Add a check that linking against the library produces working executables. Use the following C code as test:

     .. code-block:: c

        #include <uuid/uuid.h>

        int main(int argc, char * argv[]) {
          uuid_t uuid;
          uuid_generate(uuid);
          return 0;
        }

      |check_c_source_compiles| requires the test source code to be passed in as
      a *string*.
   4. If the test is successful, link executable target against the UUID library: use the
      ``PkgConfig::UUID`` target as argument to |target_link_libraries|.

   You can download the :download:`complete, working example <code/tarballs/check_source_runs_solution.tar.bz2>`.


.. keypoints::

   - You can customize the build system by executing custom commands.
   - CMake offers commands to probe compilation, linking, and execution.
