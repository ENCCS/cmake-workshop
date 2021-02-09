.. _targets:


Target-based build systems with CMake
=====================================

.. questions::

   - How can we handle more complex projects with CMake?
   - What exactly are **targets** in the CMake domain-specific language (DSL)?

.. objectives::

   - Learn that the basic elements in CMake are *not* variables, *but* targets.
   - Learn about properties of targets and how to use them.
   - Learn how to use *visibility levels* to express dependencies between targets.
   - Learn how to work with projects spanning multiple folders.
   - Learn how to handle multiple targets in one project.

Real-world projects require more than compiling a few source files into
executables and/or libraries.  In the vast majority of cases, you will be faced
with projects comprising hundreds of source files sprawling in a complex source
tree.  Using modern CMake helps you keep the complexity of the build system in
check.

It's all about targets and properties
-------------------------------------

With the advent of CMake 3.0, also known as **Modern CMake**, there has been a
significant shift in the way the CMake domain-specific language (DSL) is
structured.  Rather than relying on **variables** to convey information in a
project, we should shift to using **targets** and **properties**.

Targets
+++++++

A target is declared by either |add_executable| or |add_library|: thus, in broad
terms, a target maps to a build artifact in the project. [#custom_targets]_
Any target has a collection of **properties**, which define *how* the build
artifact should be produced **and** *how* it should be used by other dependent
targets in the project.

.. figure:: img/target.svg
   :align: center

   A target is the basic element in the CMake DSL. Each target has *properties*,
   which can be read with |get_target_property| and modified with
   |set_target_properties|.  Compile options, definitions, include directories,
   source files, link libraries, and link options are properties of targets.

It is much more robust to use targets and properties than using variables.
Given a target ``tgtA``, we can invoke one command in the ``target_*`` family as:

.. code-block:: cmake

   target_link_libraries(tgtA
     PRIVATE tgtB
     INTERFACE tgtC
     PUBLIC tgtD
     )

the use of the visibility levels will achieve the following:

- ``PRIVATE``. The property will only be used to build the target given as first
  argument.  In our pseudo-code, ``tgtB`` will only be used to build ``tgtA``
  but not be propagated as a dependency to other targets consuming ``tgtA``.
- ``INTERFACE``. The property will only be used to build targets that consume
  the target given as first argument.  In our pseudo-code, ``tgtC`` will only be
  propagated as a dependency to other targets consuming ``tgtA``.
- ``PUBLIC``. The property will be used **both** to build the target given as
  first argument **and** targets that consume it.  In our pseudo-code, ``tgtD``
  will be used to build ``tgtA`` and will be propagated as a dependency to
  any other targets consuming ``tgtA``.


.. figure:: img/target_inheritance.svg
   :align: center

   Properties on targets have **visibility levels**, which determine how CMake
   should propagate them between interdependent targets.

The five most used commands used to handle targets are:

.. signature:: |target_sources|

   .. code-block:: cmake

      target_sources(<target>
        <INTERFACE|PUBLIC|PRIVATE> [items1...]
        [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])

   Use it to specify which source files to use when compiling a target.


.. signature:: |target_compile_options|

   .. code-block:: cmake

      target_compile_options(<target> [BEFORE]
        <INTERFACE|PUBLIC|PRIVATE> [items1...]
        [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])

   Use it to specify which compiler flags to use.

.. signature:: |target_compile_definitions|

   .. code-block:: cmake

      target_compile_definitions(<target>
        <INTERFACE|PUBLIC|PRIVATE> [items1...]
        [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])

   Use it to specify which compiler definitions to use.

.. signature:: |target_include_directories|

   .. code-block:: cmake

      target_include_directories(<target> [SYSTEM] [BEFORE]
        <INTERFACE|PUBLIC|PRIVATE> [items1...]
        [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])

   Use it to specify which directories will contain header (for C/C++) and
   module (for Fortran) files.

.. signature:: |target_link_libraries|

   .. code-block:: cmake

      target_link_libraries(<target>
        <PRIVATE|PUBLIC|INTERFACE> <item>...
        [<PRIVATE|PUBLIC|INTERFACE> <item>...]...)

   Use it to specify which libraries to link into the current target.

There are additional commands in the ``target_*`` family:

.. code-block:: bash

   $ cmake --help-command-link | grep "^target_"

Properties
++++++++++

So far we have seen that you can set properties on targets, but also on tests
(see :ref:`hello-ctest`).
CMake lets you set properties at many different levels of visibility across the
project:

- **Global scope**. These are equivalent to variables set in the root
  ``CMakeLists.txt``. Their use is, however, more powerful as they can be set
  from *any* leaf ``CMakeLists.txt``.
- **Directory scope**. These are equivalent to variables set in a given leaf ``CMakeLists.txt``.
- **Target**. These are the properties set on targets that we discussed above.
- **Test**.
- **Source files**. For example, compiler flags.
- **Cache entries**.
- **Installed files**.

For a complete list of properties known to CMake:

.. code-block:: bash

   $ cmake --help-properties | less

You can get the current value of any property with:

.. signature:: |get_property|

   .. code-block:: cmake

      get_property(<variable>
             <GLOBAL
              DIRECTORY [<dir>]
              TARGET    <target>
              SOURCE    <source>
                        [DIRECTORY <dir> | TARGET_DIRECTORY <target>]
              INSTALL   <file>
              TEST      <test>
              CACHE     <entry>
              VARIABLE
             PROPERTY <name>
             [SET | DEFINED | BRIEF_DOCS | FULL_DOCS])

and set the value of any property with:

.. signature:: |set_property|

   .. code-block:: cmake

      set_property(<GLOBAL
              DIRECTORY [<dir>]
              TARGET    [<target1> ...]
              SOURCE    [<src1> ...]
                        [DIRECTORY <dirs> ...]
                        [TARGET_DIRECTORY <targets> ...]
              INSTALL   [<file1> ...]
              TEST      [<test1> ...]
              CACHE     [<entry1> ...]
             [APPEND] [APPEND_STRING]
             PROPERTY <name> [<value1> ...])


.. _multiple-folders:

Multiple folders
----------------

Each folder in a multi-folder project will contain a ``CMakeLists.txt``: a
source tree with one **root** and many **leaves**.

.. code-block:: text

   project/
   ├── CMakeLists.txt           <--- Root
   ├── external
   │   ├── CMakeLists.txt       <--- Leaf at level 1
   └── src
       ├── CMakeLists.txt       <--- Leaf at level 1
       ├── evolution
       │   ├── CMakeLists.txt   <--- Leaf at level 2
       ├── initial
       │   ├── CMakeLists.txt   <--- Leaf at level 2
       ├── io
       │   ├── CMakeLists.txt   <--- Leaf at level 2
       └── parser
           └── CMakeLists.txt   <--- Leaf at level 2

The root ``CMakeLists.txt`` will contain the invocation of the |project|
command: variables and targets declared in the root have effectively global
scope. Remember also that |PROJECT_SOURCE_DIR| will point to the folder
containing the root ``CMakeLists.txt``.
In order to move between the root and a leaf or between leaves, you will use the
|add_subdirectory| command:

.. signature:: |add_subdirectory|

   .. code-block:: cmake

      add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])

Typically, you only need to pass the first argument: the folder within the build
tree will be automatically computed by CMake.
We can declare targets at any level, not necessarily the root: a target is
visible at the level at which it is declared and all higher levels.

.. challenge:: Cellular automata

   Let's move beyond "Hello, world" and work with a project spanning multiple
   folders. We will implement a relatively simple code to compute and print to
   screen elementary `cellular automata
   <https://en.wikipedia.org/wiki/Cellular_automaton#Elementary_cellular_automata>`_.
   We separate the sources into ``src`` and ``external`` to simulate a nested project
   which reuses an external project.
   Your goal is to:

   - Build a library out of the contents of ``external`` and each subfolder of
     ``src``. Use |add_library| together with |target_sources| and, for C++,
     |target_include_directories|. Think carefully about the *visibility
     levels*.
   - Build the main executable. Where is it located in the build tree? Remember
     that CMake generates a build tree mirroring the source tree.
   - The executable will accept 3 arguments: the length, number of steps, and
     automaton rule.  You can run it with:

     .. code-block:: bash

        $ automata 40 5 30

     This is the output:

     .. code-block:: text

        length: 40
        number of steps: 5
        rule: 30
                            *
                           ***
                          **  *
                         ** ****
                        **  *   *
                       ** **** ***

   .. tabs::

      .. tab:: C++

         You can download the :download:`scaffold code <code/tarballs/21_automata-cxx.tar.bz2>`.

         The sources are organized in a tree:

         .. code-block:: text

            automata-cxx/
            ├── external
            │   ├── conversion.cpp
            │   └── conversion.hpp
            └── src
                ├── evolution
                │   ├── evolution.cpp
                │   └── evolution.hpp
                ├── initial
                │   ├── initial.cpp
                │   └── initial.hpp
                ├── io
                │   ├── io.cpp
                │   └── io.hpp
                ├── main.cpp
                └── parser
                    ├── parser.cpp
                    └── parser.hpp

         1. Should the header files be included in the invocation of
            |target_sources|? If yes, which visibility level should you use?
         2. In |target_sources|, does using absolute
            (``${CMAKE_CURRENT_LIST_DIR}/parser.cpp``) or relative
            (``parser.cpp``) paths make any difference?

         Download the :download:`complete working example <code/tarballs/21_automata-cxx_solution.tar.bz2>`.

      .. tab:: Fortran

         You can download the :download:`scaffold code <code/tarballs/21_automata-f.tar.bz2>`.

         The sources are organized in a tree:

         .. code-block:: text

            automata-f/
            ├── external
            │   └── conversion.f90
            └── src
                ├── evolution
                │   ├── ancestors.f90
                │   ├── empty.f90
                │   └── evolution.f90
                ├── initial
                │   └── initial.f90
                ├── io
                │   └── io.f90
                ├── main.f90
                └── parser
                    └── parser.f90

         1. The ``empty.f90`` source declares, as the name suggests, an empty
            Fortran module. This module is only used within the ``evolution``
            subfolder: what visibility level should it have in |target_sources|?
         2. Note that CMake can understand the compilation order imposed by the
            Fortran modules without further intervention. Where are the ``.mod``
            files?

         Download the :download:`complete working example <code/tarballs/21_automata-f_solution.tar.bz2>`.

      .. tab:: Bonus

         You can decide where executables, static and shared libraries, and
         Fortran ``.mod`` files will be stored within the build tree.
         The relevant variables are:

         - ``CMAKE_RUNTIME_OUTPUT_DIRECTORY``, for executables.
         - ``CMAKE_ARCHIVE_OUTPUT_DIRECTORY``, for static libraries.
         - ``CMAKE_LIBRARY_OUTPUT_DIRECTORY``, for shared libraries.
         - ``CMAKE_Fortran_MODULE_DIRECTORY``, for Fortran ``.mod`` files.

         Modify your ``CMakeLists.txt`` to output the ``automata`` executable in
         ``build/bin`` and the libraries in ``build/lib``.


.. callout:: The internal dependency tree

   You can visualize the dependencies between the targets in your project with Graphviz:

  .. code-block:: bash

     $ cd build
     $ cmake --graphviz=project.dot ..
     $ dot -T svg project.dot -o project.svg


  .. figure:: img/project.svg
     :align: center

     The dependencies between targets in the cellular automata project.


.. keypoints::

   - Using targets, you can achieve granular control over how artifacts are
     built and how their dependencies are handled.
   - Compiler flags, definitions, source files, include folders, link libraries,
     and linker options are **properties** of a target.
   - Avoid using variables to express dependencies between targets: use the
     visibility levels ``PRIVATE``, ``INTERFACE``, ``PUBLIC`` and let CMake
     figure out the details.
   - Use |get_property| to inquire and |set_property| to modify values of
     properties.
   - To keep the complexity of the build system at a minimum, each folder in a
     multi-folder project should have its own CMake script.


.. rubric:: Footnotes

.. [#custom_targets]

   You can add custom targets to the build system with |add_custom_target|.
   Custom targets are not necessarily build artifacts.
