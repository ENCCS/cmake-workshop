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
The difference between the two is in *when* the missing dependencies are
downloaded.  with ``ExternalProject``, the download step happens at `project
build-time <https://cmake.org/cmake/help/latest/module/ExternalProject.html>`_,
with ``FetchContent``, it will happen at `project configure-time <https://cmake.org/cmake/help/latest/module/FetchContent.html>`_.
Both are extremely powerful mechanisms, but you should use them with care.
In this episode, we will discuss the ``FetchContent`` module.


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

   In this exercise, we want to download the Catch2 project at configure-time
   from its `GitHub repository <https://github.com/catchorg/Catch2>`_.

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
      executable in the `documentation
      <https://github.com/catchorg/Catch2/blob/v2.x/docs/command-line.md#specifying-which-tests-to-run>`_.

   - What differences do you note in the configuration step?
   - What happens if you forget to issue the |FetchContent_MakeAvailable| command?

   You can download the :download:`complete, working example <code/tarballs/more-catch2_solution.tar.bz2>`.

Mixing C++ and Python with ``pybind11``
+++++++++++++++++++++++++++++++++++++++

.. warning::

   ``FetchContent`` is a powerful module in your CMake toolbox. **Beware!**
   Satisfying *every* dependency of your code in this way will make the duration
   of both the configuration and build stages balloon.



.. keypoints::

   - You can also download dependencies at configure-time with the ``FetchContent`` module.
