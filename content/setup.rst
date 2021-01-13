Setting up your system
======================

In order to follow this workshop, you will need access to compilers
and MPI libraries. You can either use a cluster or set things up on
your local computer - the instructions here are for installing on your
own computer.

We recommend that participants create an isolated software environment
on their computer and install a C compiler along with MPI libraries
inside that environment. Root-level system installation is also
possible but will not be covered here due to the risk of various
conflicts (or worse).

These instructions are based on installing compilers and MPI via the `Conda
package and enviroment manager <https://docs.conda.io/en/latest/>`_, as it
provides a convenient way to install binary packages in an isolated software
environment.

Operating systems
^^^^^^^^^^^^^^^^^

The following steps are appropriate for Linux and MacOS systems. For
Windows, it is necessary to first install the Windows Subsystem for
Linux (see these `installation instructions for WSL
<https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_).
Installing compilers and MPI natively on Windows is also possible
through `Cygwin <https://www.cygwin.com/>`_ and the Microsoft
Distribution of MPICH, but we recommend WSL which is available for
Windows 10 and later.


Installing conda
^^^^^^^^^^^^^^^^

Begin by installing Miniconda:

1. Download the 64-bit installer from `here
   <https://docs.conda.io/en/latest/miniconda.html>`_ for your operating system:

     - for MacOS and Linux, choose the bash installer
     - on Windows, open a Linux-WSL terminal and type: ``wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh``.
       If wget is not a recognised command, first install it by ``sudo apt-get install wget`` (provide the password you chose when installing WSL).
2. In a terminal, run the installer with ``bash Miniconda3-latest-<operating-system>-x86_64.sh``
   (replace with correct name of installer)
3. Agree to the terms of conditions, specify the installation directory (the default is
   usually fine), and answer "yes" to the questions "Do you wish the installer to
   initialize Miniconda3 by running conda init?"

You now have miniconda and conda installed. Make sure that it works by
typing ``which conda`` and see that it points to where you installed
miniconda (you may have to open a new terminal first).

We recommend that you create an isolated conda environment (this is
good practice in software development)::

  $ conda create --name mpi
  $ conda activate mpi

This should create a new empty environment and activate it, which
might prepend your shell prompt with the name of the conda environment.

Installing a C compiler and MPI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now install compilers and the OpenMPI
implementation of MPI::

  (mpi) $ conda install -c conda-forge compilers
  (mpi) $ conda install -c conda-forge openmpi

If you prefer MPICH over OpenMPI (or you experience problems with OpenMPI), you can
instead do::

  (mpi) $ conda install -c conda-forge compilers
  (mpi) $ conda install -c conda-forge mpich

**Please also verify the installation.**

The following commands should give version numbers::

   (mpi) $ mpicc --version
   (mpi) $ mpirun --version

With OpenMPI you can also try the ``-showme`` flag to see what the ``mpicc``
compiler wrapper does under the hood::

   (mpi) $ mpicc -showme

To compile an MPI code `hello_mpi.c`, you should now be able to do::

  (mpi) $ mpicc -o hello_mpi.x hello_mpi.c
  (mpi) $ mpirun -n 2 hello_mpi.x

To compile with OpenMP support for hybrid MPI+OpenMP codes, you need
to add the ``-fopenmp`` flag::

  (mpi) $ mpicc -fopenmp -o hello_omp_mpi.x hello_omp_mpi.c
  (mpi) $ export OMP_NUM_THREADS=2
  (mpi) $ mpirun -n 2 hello_omp_mpi.x

You *might* also need to explicitly link against the OpenMP runtime library.
