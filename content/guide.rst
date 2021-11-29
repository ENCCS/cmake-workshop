Instructor's guide
------------------

Learning outcomes
^^^^^^^^^^^^^^^^^

- Write a CMake build system for C, C++, and Fortran projects producing
  libraries and/or executables.
- Run tests for your code with CTest.
- Ensure your build system will work on different platforms.
- Detect and use external dependencies in your project.
- Safely and effectively build mixed-language projects (Python+C/C++,
  Python+Fortran, Fortran+C/C++)

Second iteration
^^^^^^^^^^^^^^^^
We decided to:

- Move the :ref:`cxx-fortran` episode to an "Additional material" section.
- Add the separate episode :ref:`python-bindings` to show how to manage
  Python+compiled language projects.
- Add the :ref:`tips-and-tricks` episode to summarize best practices.
  It was adapted from the CodeRefinery fork of this lesson: https://coderefinery.github.io/cmake-workshop/growing-projects/#growing-projects

**Day 1 - Monday 29 November 2021**

- The flow in :ref:`cmake-syntax` was not great due to the fact that I
  (@robertodr) had not double-checked carefully after rearranging the exercises.
- We had to skip the :ref:`environment` episode due to lack of time.
  This will be moved to "Additional topics" in the next iterations.

.. csv-table::
   :widths: auto
   :align: center
   :delim: ;

    9:00 -  9:10 ; Welcome and introduction to the training course
    9:10 -  9:40 ; :ref:`hello-cmake`
    9:40 -  9:45 ; Break
    9:45 - 10:15 ; :ref:`cmake-syntax`
   10:15 - 10:25 ; Break
   10:25 - 10:55 ; :ref:`hello-ctest`
   10:55 - 11:00 ; Break
   11:00 - 11:30 ; :ref:`environment`
   11:30 - 11:40 ; Break
   11:40 - 12:10 ; :ref:`probing`
   12:10 - 12:15 ; Break
   12:15 - 12:30 ; Wrap-up

**Day 2 - Tuesday 30 November 2021**

.. csv-table::
   :widths: auto
   :align: center
   :delim: ;


    9:00 -  9:10 ; What did we cover yesterday?
    9:10 -  9:50 ; :ref:`targets`
    9:50 - 10:00 ; Break
   10:00 - 10:40 ; :ref:`dependencies`
   10:40 - 10:50 ; Break
   10:50 - 11:30 ; :ref:`fetch-content`
   11:30 - 11:40 ; Break
   11:40 - 12:10 ; :ref:`python-bindings`
   12:10 - 12:15 ; Break
   12:15 - 12:45 ; :ref:`tips-and-tricks`
   12:45 - 13:00 ; Wrap-up

First iteration
^^^^^^^^^^^^^^^

**Day 1 - Tuesday 9 February 2021**

.. csv-table::
   :widths: auto
   :align: center
   :delim: ;

    9:00 -  9:10 ; Welcome and introduction to the training course
    9:10 -  9:40 ; :ref:`hello-cmake`
    9:40 -  9:45 ; Break
    9:45 - 10:15 ; :ref:`cmake-syntax`
   10:15 - 10:25 ; Break
   10:25 - 10:55 ; :ref:`hello-ctest`
   10:55 - 11:00 ; Break
   11:00 - 11:30 ; :ref:`environment`
   11:30 - 11:40 ; Break
   11:40 - 12:10 ; :ref:`probing`
   12:10 - 12:15 ; Break
   12:15 - 12:30 ; Wrap-up

**Day 2 - Wednesday 10 February 2021**

We allocated **40 minutes** to each of the :ref:`targets`, :ref:`dependencies`,
:ref:`cxx-fortran` episodes, with short breaks during the exercises in the breakout
rooms.
The :ref:`fetch-content` episode can be skipped in case contents from Day 1
spill over to Day 2.

.. csv-table::
   :widths: auto
   :align: center
   :delim: ;


    9:00 -  9:10 ; What did we cover yesterday?
    9:10 -  9:50 ; :ref:`targets`
    9:50 - 10:00 ; Break
   10:00 - 10:40 ; :ref:`dependencies`
   10:40 - 10:50 ; Break
   10:50 - 11:30 ; :ref:`cxx-fortran`
   11:30 - 11:40 ; Break
   11:40 - 12:10 ; :ref:`fetch-content`
   12:10 - 12:15 ; Break
   12:15 - 12:30 ; Wrap-up
