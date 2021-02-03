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


Custom commands for your targets
--------------------------------

.. todo::

   - |add_custom_command| with ``PRE_BUILD`` and ``POST_LINK``


Testing compilation, linking, and execution
-------------------------------------------


.. todo::

   - |try_compile| and pitfalls
   - |check_<lang>_compiler_flag|
   - |check_<lang>_source_runs|



.. keypoints::

   - You can customize the build system by executing custom commands.
   - CMake offers commands to probe compilation, linking, and execution.
