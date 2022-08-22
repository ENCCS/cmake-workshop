.. _probing:


Probing compilation, linking, and execution
===========================================

.. questions::

   - How can you add custom steps to your build system with CMake?

.. objectives::

   - Learn how and when to use |execute_process|
   - Learn how to use |add_custom_command| with targets.
   - Learn how to test compilation, linking, and execution.


CMake lets you run arbitrary commands at any stage in the project lifecycle.
This is yet another mechanism for fine-grained customization and we will discuss
some of the options in this episode.


Running custom commands at *configure-time*
-------------------------------------------

The most straightforward method is to explicitly run one (or more) child
process(es) when invoking the ``cmake`` command.  This is achieved with the
|execute_process| command.

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
   respectively. The result of the last child process is saved into
   ``RESULT_VARIABLE``.


It is important to note that any command invoked through ``execute_process``
will only be run at **configure-time**, *i.e.* when running the ``cmake``
command. You **should not** rely on |execute_process| to update any artifacts at
**build-time**.


.. exercise:: Exercise 17: Find a Python module

   In this exercise, we'll use |execute_process| to check whether the `cffi
   <https://cffi.readthedocs.io/en/latest/index.html>`_ Python module is
   installed in your environment. On the command line, you would do:

   .. code-block:: bash

      $ python -c "import cffi; print(cffi.__version__)"

   Your goal is to replicate the same in CMake.
   The scaffold code is in ``content/code/day-1/17_find_cffi``.
   You will have to modify the call to |execute_process| to run the command above.

   A working example is in the ``solution`` subfolder.

Note the use of ``find_package(Python REQUIRED)`` to obtain the ``python``
executable. CMake comes with many modules dedicated to the detection of
dependencies, such as Python. These are conventionally called
``Find<dependency>.cmake`` and you can inspect their documentation with:

.. code-block:: bash

   $ cmake --help-module FindPython | more

We will revisit uses of |find_package| later on in :ref:`dependencies`.


Custom commands for your targets
--------------------------------

As mentioned, the main problem of |execute_process| is that it will run a
command at *configure-time*, when the ``cmake`` command is first invoked.
It is thus *not* a viable alternative if we intend to perform some specific
actions depending on targets or make the result of the custom commands a
dependency for other targets.
Both cases have real-world examples, such as when using automatically generated
code. The CMake command |add_custom_command| can be used in some of this
instances.

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


.. exercise:: Exercise 18: Before and after build

   We want to perform some action before and after building a target, in this case a Fortran executable:

   - Before building, we want to read the link line, as produced by CMake, and
     echo it to standard output. We use the ``echo-file.py`` Python script.
   - After building, we want to check the size of the static allocations in the
     binary, by invoking the ``size`` command. We use the ``static-size.py`` Python script.

   The scaffold code is in ``content/code/day-1/18_pre_post-f``.

   #. Add CMake commands to build the ``example`` executable from the Fortran
      sources.  Find the text file with the link line under the build folder.
      Hint: have a look in ``CMakeFiles`` and keep in mind the name you gave to
      the target.
   #. Call |add_custom_command| with ``PRE_LINK`` to invoke the ``echo-file.py`` Python script.
   #. Call |add_custom_command| with ``POST_BUILD`` to invoke the ``static-size.py`` Python script.

   A working example is in the ``solution`` subfolder.


Testing compilation, linking, and execution
-------------------------------------------

We also want to be able to run checks on our compilers and linkers. Or check whether a certain library can be used correctly before attempting to build our own artifacts.
CMake provides modules and commands for these purposes:

- ``Check<LANG>CompilerFlag`` providing the ``check_<LANG>_compiler_flag``
  function, to check whether a compiler flag is valid for the compiler in use.
- ``Check<LANG>SourceCompiles`` providing the ``check_<LANG>_source_compiles``.
  Which check whether a given source file compiles with the compiler in use.
- ``Check<LANG>SourceRuns`` providing the ``check_<LANG>_source_runs``, to make
  sure that a given source snippet compiles, links, and runs.

In all cases, ``<LANG>`` can be one of ``CXX``, ``C`` or ``Fortran``.

.. exercise:: Exercise 19: Check that a compiler accepts a compiler flag

   Compilers evolve: they add and/or remove flags and sometimes you will face
   the need to test whether some flags are available before using them in your
   build.

   The scaffold code is in ``content/code/day-1/19_check_compiler_flag``.

   #. Implement a ``CMakeLists.txt`` to build an executable from the
      ``asan-example.cpp`` source file.
   #. Check that the address sanitizer flags are available with
      |check_cxx_compiler_flag|. The flags to check are ``-fsanitize=address
      -fno-omit-frame-pointer``. Find the command signature with:

      .. code-block:: bash

         $ cmake --help-module CMakeCXXCompilerFlag

   #. If the flags do work, add them to the those used to compile the executable
      target with |target_compile_options|.

   A working example is in the ``solution`` subfolder.


.. exercise:: Exercise 20: Testing runtime capabilities

   Testing that some features will work properly for your code requires not only
   compiling an object files, but also linking an executable and running it
   successfully.

   The scaffold code is in ``content/code/day-1/20_check_source_runs``.

   #. Create an executable target from the source file ``use-uuid.cpp``.
   #. Add a check that linking against the library produces working executables.
      Use the following C code as test:

      .. code-block:: c

         #include <uuid/uuid.h>

         int main(int argc, char * argv[]) {
           uuid_t uuid;
           uuid_generate(uuid);
           return 0;
         }

      |check_c_source_runs| requires the test source code to be passed in as
      a *string*. Find the command signature with:

      .. code-block:: bash

         $ cmake --help-module CheckCSourceRuns

   #. If the test is successful, link executable target against the UUID
      library: use the ``PkgConfig::UUID`` target as argument to
      |target_link_libraries|.

   A working example is in the ``solution`` subfolder.


.. keypoints::

   - You can customize the build system by executing custom commands.
   - CMake offers commands to probe compilation, linking, and execution.
