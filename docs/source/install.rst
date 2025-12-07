:orphan:

Installation
============

In this section, we will see how **appLP** can be installed in your Python projects.

1. We will first do a quick :ref:`reminder on CLI basics <cli_reminder>` necessary to install comfortably the library.
2. Then, we will explain how to :ref:`create a fresh project <create_project>` compatible with it using *uv*.
3. Finally, we will show how to :ref:`contribute to the source code development <get_source_code>` by cloning the repository with *git*.

.. _cli_reminder:

1. CLI reminder
---------------

For installation, you will need to use a **Command Line Interface** (CLI) like your system terminal.
If you are using Windows or macOS, you might not be familiar with these, so we will first do a quick reminder for these two OS.

If you are using Linux, I suppose you will not need these and you can skip to the :ref:`project creation part <create_project>`.

.. _opening_the_terminal:

Opening the terminal
~~~~~~~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Windows

      First, you will need to open a terminal window:
      search for ``Windows PowerShell`` in the *Start Menu* (or press **Win + R**, type ``PowerShell``, then press **Enter**)
      
      A terminal window will appear with something like:
      
      .. code-block:: PowerShell

         PS C:\Users\myusername> _

   .. tab-item:: macOS

      First, you will need to open a terminal window:
      open **Applications → Utilities → Terminal** (or press **Cmd + Space**, type ``Terminal``, and press **Enter**)
      
      A terminal window will appear with something like:
      
      .. code-block:: PowerShell

         MacBook:~ myusername$ _

When the cursor (``_``) is blinking, it means you can type a command.  
The path you see on the left of the line is your **current directory**—the folder from which commands will be executed.

Commands generally follow this structure:

      .. code-block:: shell

         command-name argument --option1 value --option2 value

Options usually start with ``--option-name``, but one-letter shortcuts like ``-y`` for ``--yes`` may exist.
When a command is known by your system, you can type the beginning and press **Tab** to auto-complete it.
To learn more about available commands and their options, refer to online documentation (or ask your favorite AI assistant).

.. warning::

   For real noobs like me who come from Python courses, you might be used to Python editors ("IDE" = **Integrated Development Environment**) with a shell.
   Therefore, you might think the PowerShell command lines accept Python commands, **which is wrong**.
   
   The Python editors shell launch under the hood a Python interpreter.
   You can identify if you are in a Python interpreter as the Python CLI starts with
   
   .. code-block:: shell

      >>> _

   To launch a Python interpreter in the terminal and get the same behavior as your Python editors, you need to have Python installed on your machine and write ``python`` to open the interpreter.

.. _navigation_commands:

Navigation commands
~~~~~~~~~~~~~~~~~~~

In the OS terminal, `cd` (**Change Directory**) lets you move between folders.

.. tab-set::

   .. tab-item:: Windows

      In Windows, folders are separated by ``\``

      ``cd`` command can be used various ways:

      - change directory using an absolute path: ``cd full\path\to\new\directory``
      - go to the parent folder: ``cd ..``
      - navigate to a folder inside your current directory: ``cd relative\path\inside\current\directory``
      - combine movements, for example to reach a folder inside the grandparent directory:  ``cd ..\..\relative\path\to\folder``
      - go to your user home directory: ``cd ~``

   .. tab-item:: macOS

      In macOS, folders are separated by ``/`` (like in Linux)

      ``cd`` command can be used various ways:
   
      - change directory using an absolute path: ``cd full/path/to/new/directory``
      - go to the parent folder: ``cd ..``
      - navigate to a folder inside your current directory: ``cd relative/path/inside/current/directory``
      - combine movements, for example to reach a folder inside the grandparent directory:  ``cd ../../relative/path/to/folder``
      - go to your user home directory: ``cd ~``
      - go back to previous directory (macOS only): ``cd -``

.. _folder_management_commands:

Folder management commands
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Windows

      - list folders and files in current **directory**: ``dir``
      - **make** a new **directory** (=folder): ``mkdir MyFolderName``
      - **remove** a **directory**: ``rmdir MyFolderName``
      - **delete** a file: ``del MyFile.txt``

   .. tab-item:: macOS

      - **list** folders and files in current directory: ``ls``
      - **make** a new **directory** (=folder): ``mkdir MyFolderName``
      - **remove** a directory (**recursive** delete): ``rm -r MyFolderName``
      - **remove** a file: ``rm MyFile.txt``

.. _create_project:

2. Create project
-----------------

Here, we want to create a new Python project with a dependency on **appLP**.
To make this kind of project functional, there are several steps to follow :

- :ref:`initialize the project folder <initialize_project_with_uv>`:

   1. define a *pyproject.toml* file to write dependencies and other metadata
   2. define a *README.md* file for documentation notes and explanations
   3. add dependencies

- :ref:`create a virtual environment <create_virtual_environment_with_uv>`:

   1. Solve the dependencies versions
   2. install Python on your machine
   3. create a virtual environment
   4. activate the virtual environment
   5. install dependencies

- :ref:`run the script from a fresh terminal <run_script_with_virtual_environment>`:

   1. activate the virtual environment
   2. run the script

As these are tedious to achieve manually, I highly recommend using `uv <https://docs.astral.sh/uv/getting-started/installation/>`_ from *Astral* for installation and environment management as it is a very fast and all-in-one solution.

However, if you do not want to use *uv*, for example if you are used to using *Anaconda distribution*, or for any other reason, we will also show how to initialize the project without *uv* at the :ref:`end of this subsection <create_project_without_uv>`.

.. dropdown:: If *uv* is not installed (or you are unsure)
   :icon: chevron-down

   To check if *uv* is installed, you can try the following command.
   If it gives you a version, than *uv* is already installed!

   .. code-block:: shell

      uv --version

   If it fails, you need to install *uv*.

   .. tab-set::

      .. tab-item:: Linux

         you can install with *curl*:

         .. code-block:: shell

            curl -LsSf https://astral.sh/uv/install.sh | sh

         If *curl* did not seem to be installed, install it before following the command corresponding to your distro:

         - **Debian** and **Ubuntu**: ``sudo apt update && sudo apt install curl -y``
         - **Fedora**: ``sudo dnf install curl -y``
         - **Arch Linux** and **Manjaro**: ``sudo pacman -S curl``

      .. tab-item:: Windows

         I recommand using a package manager for the installation. You can use one the following:

         - `WinGet <https://winstall.app/>`_: ``winget install --id=astral-sh.uv  -e``
         - `Scoop <https://scoop.sh/>`_: ``scoop install main/uv``
         - `Chocolatey <https://chocolatey.org/install>`_: ``choco install uv``

         If you want to install *uv* using standalone installers or other methods, please refer to their `uv Windows installation website <https://docs.astral.sh/uv/getting-started/installation/>`_

      .. tab-item:: macOS

         I recommand using a package manager for the installation. You can use one the following:

         - `Homebrew <https://brew.sh/>`_: ``brew install uv``
         - curl: Follow the same steps as for the Linux protocole.
         - `MacPorts <https://www.macports.org/install.php>`_: ``sudo port selfupdate && sudo port install uv``

         If you want to install *uv* using standalone installers or other methods, please refer to `uv macOSinstallation website <https://docs.astral.sh/uv/getting-started/installation/>`_

   Now *uv* should be installed on your macOS machine!

.. _initialize_project_with_uv:

Initialize a project with *uv*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's assume we changed directory with ``cd`` to the parent folder of our future project.
To initialize a project called `my_project` with *uv*, use command:

.. code-block:: shell

   uv init my_project
   cd my_project

This will create a folder with a *pyproject.toml* file, a *README.md* file and a *main.py* file, then change directory inside the project.

Then, we just need to add the dependencies to your project, typically dependency to **appLP**, with the command:

.. code-block:: shell

   uv add applp

You can redo this command for all the dependencies you might need by replacing the "appLP" by the other dependency name (the name ususally used in the command ``pip``).
For more informations, go to the `uv project <https://docs.astral.sh/uv/guides/projects/>`_ website.

The project is now initialized!

.. _create_virtual_environment_with_uv:

Create virtual environment with *uv*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With *uv*, you can do all five steps defined for the Python virtual environment definition above at once. First go to the project directory with ``cd path_to_my_project`` (replace ``path_to_my_project``).

*uv* can then:

1. look at the *pyproject.toml* file and solve the Python & dependencies versions that are necessary by storing them in a *uv.lock* file
2. look if the necessary Python distribution is in your machine, if not will download it online
3. look if you have already a virtual environment folder (*.venv*), if not will create it
4. activate the *.venv*
5. look if all dependencies versions are installed, if not will install them from *pip*

*uv* gives you commands if you want to do these individually:

- step 1 only: ``uv lock``
- step 2 only: ``uv python install``
- step 3 to 4: ``uv venv``
- step 1 to 5: ``uv sync``

For more informations, go to the `uv commands <https://docs.astral.sh/uv/reference/cli/>`_ website.

But in fact, to create the virtual environment from scratch, you only need to use:

.. code-block:: shell

   uv sync

The project virtual environment *.venv* should now be created!

.. _run_script_with_virtual_environment:

Run script with virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your project virtual environment is set, to run a script *my_script.py* from a fresh system terminal you need to activate the *.venv* and run your script inside.
*uv* gives a single command for that:

.. code-block:: shell

   uv run my_script.py

The advantage using this command is that it always calls ``uv sync`` under the hood, so if the virtual environment is not set, or is not up to date, it will be created automatically. 
For more information on script dependencies, please refer to the `uv script <https://docs.astral.sh/uv/guides/scripts/>`_ website.

In practice, Python scripts are often launched from an editor.
The complicated part is to use the virtual environment we previously created with these editors.
In the following tabs are the protocoles for most commonly used editors.

.. tab-set::

   .. tab-item:: Visual Studio Code

      The console in **Visual Studio Code** (or any wrapper editor like **Cursor**) is a system terminal, so if you installed *uv* as suggested, you can just use :
   
      .. code-block:: shell

         uv run my_script.py

      **Visual Studio Code** also proposes a *Python extension* to give the ability to run scripts via a button (IPython under the hood).

      If you use this button, be aware that the *.venv* environment needs to be activated.
      If you opened **Visual Studio Code** in the *.venv* parent folder, it should auto-activate if the feature is enabled (by default the setting is ON).
      If you want to activate it manually: 

      1. Press **Ctrl + Shift + P** (Linux and Windows) or **Cmd + Shift + P** (macOS)
      2. Run: `Python: Select Interpreter`
      3. Choose the interpreter inside your venv, usually shown as:

         .. code-block:: bash

            ./.venv/bin/python       (Linux/Mac)
            ./.venv/Scripts/python.exe (Windows)

      4. Open new terminal window

   .. tab-item:: Anaconda tools (Spyder Jupyter)

      If you are using *Anaconda*, you probably are coding via *Spyder* and *Jupyter*.

      By default, these use the *base* environment of *Anaconda*, so when you launch them the virtual environment we created will not be active.
      To be able to use another virtual environment, *Spyder* and *Jupyter* connects to specific kernels, respectively *spyder-kernels* and *ipykernel*, which are included in **appLP** library dependencies.

      To activate the virtual environment manually inside the GUIs:

      - Spyder: ``Preferences → Python Interpreter``
      - Jupyter: ``Kernel → Change Kernel``

      ... and choose the interpreter inside your venv, usually shown as:

      .. code-block:: bash

         ./.venv/bin/python       (Linux/Mac)
         ./.venv/Scripts/python.exe (Windows)

   .. tab-item:: Other editors

      As other editors have not been tested, please refer to dedicated support to run scripts from virtual environments with these.

To finish, some scripts may be provided with the library **appLP** :doc:`(see Reference Guide) <scripts>`.
To use them, you can just download `scripts source codes <https://github.com/LancelotPincet/appLP/tree/main/src/applp/scripts>`_.

.. _create_project_without_uv:

Create project without *uv*
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you do not like *uv* or are used to other tools, you can explore other possibilities to create your projects by using the dropdown menus bellow.

.. dropdown:: Using *Anaconda* distribution
   :icon: chevron-down

   *Anaconda* is a Python distribution designed for scientific programming.

   To install *Anaconda*, you can:

   - Use an installer corresponding to your OS. If you go directly on `their archive website <https://repo.anaconda.com/>`_, you will not need to create an account to download the installer, which is the "forced way" if you follow the classic procedure from their `homepage <https://www.anaconda.com/download>`_
   - Use a command corresponding to your OS described in their `documentation <https://www.anaconda.com/docs/getting-started/anaconda/install>`_

   By default in Windows, *Anaconda* is not added to the *PATH*, so ``conda`` commands will not work in the system terminal, for these use the *Anaconda prompt* provided with the distribution.

   In *Anaconda*, virtual environments are not stored in the project folder, but in the *anaconda3* folder.
   The philosophy is not to have one virtual environment per project, but to have several projects with same non-conflicting dependencies sharing a global virtual environment.
   That is why *Anaconda* does not provide tools to initialize projects.
   Here we will explain how to setup up virtual environments dependent on **appLP** that you will be able to use on various projects.

   By default, you will have a *base* virtual environment where all the classical scientific libraries are already installed.
   This is the virtual environment use by default by the tools from Anaconda like *Spyder* or *Jupyter Lab*.
   However some dependencies for this Python project might not be available in this *base* environment, like **appLP**.
   You could manually add these but **this is not recommended** as it will pollute your *base* environment for your other projects and might at some point create dependencies conflicts.

   Best practice is to create a new virtual environment and work dependencies inside.
   Use these commands in the *Anaconda prompt* to set up a virtual environment :

   - create venv: ``conda create -n venv_appLP python``
   - activate venv: ``conda activate venv_appLP``
   - update pip: ``conda install pip``
   - add *Spyder* and *Jupyter* kernels: ``conda install spyder-kernels ipykernel``
   - install **appLP**: ``pip install applp``
   - ...for all other dependencies: ``conda install my_dependency_name` or `pip install my_dependency_name``

   Now that the venv is ready in your anaconda3 folder, to run a script from a freshly opened terminal:

   .. code-block:: bash

      conda activate venv_appLP
      python full/path/to/my_script.py

   Then you can deactivate the virtual environment if needed with ``conda deactivate``

   You can also use *Spyder* or *Jupyter* to run scripts with a virtual environment like it was explained :ref:`above <run_script_with_virtual_environment>` 

.. dropdown:: Manual project
   :icon: chevron-down

   If you do not want to use any external tool and have lots of patience, you can do each step manually.

   1. Install Python from the `website <https://www.python.org/downloads/>`_
   2. Create a new project folder
   3. For good practices, you can add *README.md* and *pyproject.toml* files manually
   4. Create a virtual environment inside the project folder from terminal: ``python -m venv .venv``
   5. Activate the virtual environment: ``.\.venv\Scripts\Activate.ps1`` in Windows, ``source .venv/bin/activate`` in Linux/macOS
   6. Install **appLP** from terminal: ``pip install applp``
   7. Install with pip all the other dependencies by hand: ``pip install mydependency==myversion``

   With these, the project folder should be initialized with a virtual environment.

   Then to launch a script from a fresh terminal:

   - Activate the virtual environment: ``.\.venv\Scripts\Activate.ps1`` in Windows, ``source .venv/bin/activate`` in Linux/macOS
   - Run script: ``python full/path/to/my_script.py``

.. _get_source_code:

3. Get source code
------------------

If ever you want to play with the library source code, to apply your own modifications, or even to contribute, you can access it on the `GitHub page <https://github.com/LancelotPincet/appLP>`_.

You could download the project directly from the website, but this is **not recommended** as you will not be able to follow various versions of the project, and your modifications will be incompatible with these.
It is recommended to take the habit of using *git*.

.. dropdown:: If *git* is not installed (or you are unsure)
   :icon: chevron-down

   To check if *git* is installed, you can try the following command.
   If it gives you a version, than *git* is already installed!

   .. code-block:: shell

      git --version

   If it fails, you need to install *git*.

   .. tab-set::

      .. tab-item:: Linux

         *git* is often installed by default in Linux.
         If it is not the cas, use one of following the command corresponding to your distro:

         - **Debian** and **Ubuntu**: ``sudo apt update && sudo apt install git -y``
         - **Fedora**: ``sudo dnf install git -y``
         - **Arch Linux** and **Manjaro**: ``sudo pacman -S git --noconfirm``

         If you want to install *git* using standalone installers or other methods, please refer to their `git Linux installation website <https://git-scm.com/install/linux>`_

      .. tab-item:: Windows

         I recommand using a package manager for the installation. You can use one the following:

         - `WinGet <https://winstall.app/>`_: ``winget install --id Git.Git -e --source winget``
         - `Scoop <https://scoop.sh/>`_: ``scoop install git``
         - `Chocolatey <https://chocolatey.org/install>`_: ``choco install git``

         If you want to install *git* using standalone installers or other methods, please refer to  `git Windows installation website <https://git-scm.com/install/windows>`_

      .. tab-item:: macOS

         I recommand using a package manager for the installation. You can use one the following:

         - `Homebrew <https://brew.sh/>`_: ``brew install git``
         - Xcode: ``xcode-select --install``
         - `MacPorts <https://www.macports.org/install.php>`_: ``sudo port selfupdate && sudo port install git``

         If you want to install *git* using standalone installers or other methods, please refer to their `git macOS installation website <https://git-scm.com/install/mac>`_

   Now *git* should be installed on your macOS machine!

.. _clone_library_with_git:

Clone library with *git*
~~~~~~~~~~~~~~~~~~~~~~~~

First, you need to configure your *git* global parameters by filling your name and adress email:

.. code-block:: shell

   git config --global user.name "Your Name"
   git config --global user.email "youremail@example.com"

Now, you can clone in your current directory the `source code folder <https://github.com/LancelotPincet/appLP>`_ with the following command

.. code-block:: shell

   git clone https://github.com/LancelotPincet/appLP.git

The project source code should then be present in your local folder.
If you want to contribute, you can do a pull-request in the GitHub repository.