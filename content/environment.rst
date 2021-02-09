.. _environment:


Detecting your environment
==========================

.. questions::

   - How does CMake interact with the host environment?

.. objectives::

   - Learn how to discover the operating system.
   - Learn how to discover processor characteristics.
   - Learn how to handle platform- and compiler-dependent source code.


CMake comes pre-configured with sane defaults for a multitude of properties of
the environments in which it can be used.  Default generator, default compilers,
and compiler flags are few and most notable examples of this up-front
configuration.
Run the following:

.. code-block:: bash

   $ cmake --system-information | less


if you are curious about what kind of configuration ships for your version of
CMake and operating system.

In this episode, we will show how to use CMake to introspect the environment in
which we are running. This is very common in build systems, since it allows to
customize the creation of artifacts on-the-fly.


.. typealong:: Discovering the operating system

   For this example, we use the special value ``NONE`` for the ``LANGUAGES``
   option: we are only interested in reporting what operating system CMake
   discovers and that is independent of programming language.

   You can download the :download:`complete, working example <code/tarballs/12_OS_solution.tar.bz2>`.


Discovering the processor
-------------------------

A common customization is to apply processor-specific compiler flags. We can gain
such information on the host system with the built-in
|cmake_host_system_information| command.

.. signature:: |cmake_host_system_information|

   .. code-block:: cmake

      cmake_host_system_information(RESULT variable QUERY <key> ...)

   This commands accepts one or more queries on the host system and returns the result in the ``variable``.


.. typealong:: Processor discovery

   Once again, we use the special value ``NONE`` for the ``LANGUAGES`` option:
   we are only interested in reporting what CMake discovers about the host
   system and that is independent of programming language.

   You can download the :download:`complete, working example <code/tarballs/13_processor_solution.tar.bz2>`.


.. challenge:: Get to know your host

   1. Get the scaffold code from the :download:`previous type-along
      <code/tarballs/13_processor_solution.tar.bz2>`.
   2. Open the help page for |cmake_host_system_information|. Either in the browser or in the command-line:

      .. code-block:: bash

         $ cmake --help-command cmake_host_system_information

   3. Extend the scaffold code to query all keys listed in the help page and
      print them out.

   You can download the :download:`complete, working example <code/tarballs/14_host_system_information_solution.tar.bz2>`.


Platform- and compiler-dependent source code
--------------------------------------------


.. typealong:: Conditional compilation with preprocessor definitions

   Sometimes we need to write code that performs different operations based on
   compile-time constants:

   .. code-block:: c++

      #ifdef IS_WINDOWS
        return std::string("Hello from Windows!");
      #elif IS_LINUX
        return std::string("Hello from Linux!");
      #elif IS_MACOS
        return std::string("Hello from macOS!");
      #else
        return std::string("Hello from an unknown system!");
      #endif

   We can achieve this with CMake with a combination of host system
   introspection and the |target_compile_definitions| command.

   You can download the :download:`complete, working example <code/tarballs/15_sys_preproc_solution.tar.bz2>`.

.. signature:: |target_compile_definitions|

   .. code-block:: cmake

      target_compile_definitions(<target>
        <INTERFACE|PUBLIC|PRIVATE> [items1...]
        [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])

   Adds one (or more) compile definitions to the given ``<target>``.


It might be more convenient to have a single file containing all these
compile-time constants, rather than passing them to preprocessor. This can be
achieved by having a *scaffold* file and then letting CMake configure it after
discovering the values for all the necessary compile-time constants.


.. signature:: |configure_file|

   .. code-block:: cmake

      configure_file(<input> <output>
                     [COPYONLY] [ESCAPE_QUOTES] [@ONLY]
                     [NEWLINE_STYLE [UNIX|DOS|WIN32|LF|CRLF] ])

   Copies the ``<input>`` file to another file ``<output>``, modifying its content.


.. challenge:: Configure a file

   Let's revisit one of the previous exercises. Rather than print the results of
   querying with |cmake_host_system_information|, we want to save the results to
   a header file and then use it to print the results when running an
   executable.

   1. Get the :download:`scaffold code <code/tarballs/16_configure.tar.bz2>`.
      The header file ``config.h.in`` contains placeholders for the values that
      CMake will detect.
   2. Adapt the ``CMakeLists.txt`` in the previous exercise to compile
      ``processor-info.cpp`` into an executable.
   3. Try building. This should fail, because there is no ``config.h`` file anywhere yet!
   4. Open the help page for |configure_file|. Either in the browser or in the command-line:

      .. code-block:: bash

         $ cmake --help-command configure_file

   5. Query all keys listed in the help page for |cmake_host_system_information|
      and save them to appropriately named variables.
   6. Invoke |configure_file| to produce ``config.h`` from ``config.h.in``.
   7. Try building again. This will fail too, because the header is not in the *include path*. We can fix this with:

      .. code-block:: cmake

         target_include_directories(processor-info
           PRIVATE
             ${PROJECT_BINARY_DIR}
           )

   You can download the :download:`complete, working example <code/tarballs/16_configure_solution.tar.bz2>`.


.. keypoints::

   - CMake can *introspect* the host system.
   - You can build source code differently, based on the OS, the processor, the
     compiler, or any combination thereof.
   - You can generate source code when configuring the project with |configure_file|.
