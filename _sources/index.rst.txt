CMake hands-on workshop
=======================


CMake is a language-agnostic, cross-platform build tool and is nowadays the *de
facto* standard,  with large projects using it to reliably build, test, and
deploy their codebases. You will learn how to:

- Write a CMake build system for C, C++, and Fortran projects producing
  libraries and/or executables.
- Run tests for your code with CTest.
- Ensure your build system will work on different platforms.
- Detect and use external dependencies in your project.
- Safely and effectively build mixed-language projects (Python+C/C++,
  Python+Fortran, Fortran+C/C++)


.. prereq::

   Before attending this workshop, please make sure that you have access
   to a computer with a compiler for your favorite language and a recent version of CMake.
   If you have access to a supercomputer (e.g. a `SNIC system
   <https://supr.snic.se/>`_) with a compute allocation you can use that during
   the workshop. Any questions on how to use a particular HPC resource should be
   directed to the appropriate support desk.
   You can also use your own computer for this workshop, provided that it has
   the necessary tools installed. If you do not already have these
   installed, we recommend that you set up an isolated software environment
   using ``conda``. For Windows computers we recommend to use the Windows
   Subsystem for Linux (WSL). Detailed instructions can be found
   on the :doc:`setup` page.


.. toctree::
   :hidden:
   :maxdepth: 1

   setup


.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: The lesson

   hello-cmake
   cmake-syntax
   hello-ctest
   environment
   probing
   targets
   dependencies
   cxx-fortran
   fetch-content


.. see also the schedule in guide.rst

.. csv-table::
   :widths: auto
   :delim: ;

   30 min ; :doc:`hello-cmake`
   30 min ; :doc:`cmake-syntax`
   30 min ; :doc:`hello-ctest`
   30 min ; :doc:`environment`
   30 min ; :doc:`probing`
   40 min ; :doc:`targets`
   40 min ; :doc:`dependencies`
   40 min ; :doc:`cxx-fortran`
   30 min ; :doc:`fetch-content`


.. toctree::
   :maxdepth: 1
   :caption: Reference

   quick-reference
   zbibliography
   guide



.. _learner-personas:

Who is the course for?
----------------------

This course is for students, researchers, engineers, and programmers that have
heard of `CMake`_ and want to learn how to use it effectively with projects they
are working on.
This course assumes no previous experience with `CMake`_. You will have to be
familiar with the tools commonly used to build software in your compiled
language of choice: C++, C, Fortran.
Specifically, this lesson assumes that participants have some prior experience
with or knowledge of the following topics (but no expertise is required):

- Compiling and linking executables and libraries.
- Differences between shared and static libraries.
- Automated testing.



About the course
----------------

This lesson material is developed by the `EuroCC National Competence Center
Sweden (ENCCS) <https://enccs.se/>`_ and taught in ENCCS workshops. It is aimed
at researchers and developers who might have had some exposure to `CMake`_ and
want to learn how to use it effectively. This lesson targets **CMake >=3.14**.
Each lesson episode has clearly defined learning objectives and includes
multiple exercises along with solutions, and is therefore also useful for
self-learning.
The lesson material is licensed under `CC-BY-4.0
<https://creativecommons.org/licenses/by/4.0/>`_ and can be reused in any form
(with appropriate credit) in other courses and workshops.
Instructors who wish to teach this lesson can refer to the :doc:`guide` for
practical advice.


Graphical and text conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We adopt a few conventions which help organize the material.

Function signatures
   These are shown in a text block marked with a wrench emoji:

   .. signature:: |cmake_minimum_required|

      .. code-block:: cmake

         cmake_minimum_required(VERSION <min>[...<max>] [FATAL_ERROR])

   The signature can be hidden by clicking the toggle.

Command parameters
   The description of the command parameters will appear in a separate text
   box. It will be marked with a laptop emoji:

   .. parameters::

      ``VERSION``
          Minimum and, optionally, maximum version of CMake to use.
      ``FATAL_ERROR``
          Raise a fatal error if the version constraint is not satisfied. This
          option is ignored by CMake >=2.6

   The description is hidden and will be shown by clicking the toggle.

Type-along
   The text and code for these activities are in a separate text box, marked with
   a keyboard emoji:

   .. typealong:: Let's look at an example

      .. code-block:: cmake

         cmake_minimum_required(VERSION 3.16)

         project(Hello LANGUAGES CXX)

   The content can be hidden by clicking the toggle.



See also
--------

There are many free resources online regarding CMake:

- The `CMake official documentation
  <https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html>`_.
- The `CMake tutorial <https://cmake.org/cmake/help/v3.19/guide/tutorial/index.html#guide:CMake%20Tutorial>`_.
- The `HEP Software Foundation <https://hsf-training.github.io/hsf-training-cmake-webpage/>`_ training course.


You can also consult the following books:

- **Professional CMake: A Practical Guide** by Craig Scott.
- **CMake Cookbook** by Radovan Bast and Roberto Di Remigio. The accompanying repository is on `GitHub <https://github.com/dev-cafe/cmake-cookbook>`_


Credits
-------

The lesson file structure and browsing layout is inspired by and derived from
`work <https://github.com/coderefinery/sphinx-lesson>`_ by `CodeRefinery
<https://coderefinery.org/>`_ licensed under the `MIT license
<http://opensource.org/licenses/mit-license.html>`_. We have copied and adapted
most of their license text.

Instructional Material
^^^^^^^^^^^^^^^^^^^^^^

All ENCCS instructional material is made available under the `Creative Commons
Attribution license (CC-BY-4.0)
<https://creativecommons.org/licenses/by/4.0/>`_. The following is a
human-readable summary of (and not a substitute for) the `full legal text of the
CC-BY-4.0 license <https://creativecommons.org/licenses/by/4.0/legalcode>`_.
You are free:

- to **share** - copy and redistribute the material in any medium or format
- to **adapt** - remix, transform, and build upon the material for any purpose,
  even commercially.

The licensor cannot revoke these freedoms as long as you follow these license terms:

- **Attribution** - You must give appropriate credit (mentioning that your work
  is derived from work that is Copyright (c) ENCCS and, where practical, linking
  to `<https://enccs.se>`_), provide a `link to the license
  <https://creativecommons.org/licenses/by/4.0/>`_, and indicate if changes were
  made. You may do so in any reasonable manner, but not in any way that suggests
  the licensor endorses you or your use.
- **No additional restrictions** - You may not apply legal terms or
  technological measures that legally restrict others from doing anything the
  license permits. With the understanding that:

  - You do not have to comply with the license for elements of the material in
    the public domain or where your use is permitted by an applicable exception
    or limitation.
  - No warranties are given. The license may not give you all of the permissions
    necessary for your intended use. For example, other rights such as
    publicity, privacy, or moral rights may limit how you use the material.
  
Software
^^^^^^^^

The code samples and exercises in this lesson were adapted from the GitHub
repository for the `CMake Cookbook <https://github.com/dev-cafe/cmake-cookbook>`_.

Except where otherwise noted, the example programs and other software provided
by ENCCS are made available under the `OSI <http://opensource.org/>`_-approved
`MIT license <http://opensource.org/licenses/mit-license.html>`_.
