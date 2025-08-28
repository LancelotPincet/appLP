Installation
============

**appLP** uses `uv <https://docs.astral.sh/uv>`_ from *Astral* for installation and environment management.
As it is simple and has an all-in-one solution, switching your project to *uv* is highly recommended if you do not use it yet.

1. Install uv
-------------

For installation, the simplest way is to use a package manager like ``Winget`` or ``Scoop`` on Windows, and ``Homebrew`` on Linux and macOS.

For using `Winget <https://winstall.app/apps/astral-sh.uv>`_, write in PowerShell:

.. code-block:: powershell

   winget install --id=astral-sh.uv -e

For using `Scoop <https://scoop.sh/#/apps?q=uv>`_, write in PowerShell:

.. code-block:: powershell

   scoop install main/uv

For using Homebrew, write in bash:

.. code-block:: bash

   brew install uv

If you still want to install uv using standalone installers or other methods, please refer to their `installation website <https://docs.astral.sh/uv/getting-started/installation/>`_.



2. Create a project using uv
----------------------------

To create a project with a dependency on **appLP**, just type in your console by filling ``PATH_TO_PROJECT_PARENT``:

.. code-block:: shell

   cd PATH_TO_PROJECT_PARENT
   uv init my_project
   cd my_project

Then just add your project dependency to **appLP**:

.. code-block:: shell

   uv add appLP
   uv sync

Now your virtual environment with **appLP** should appear in your project folder as *.venv*. 
For more information on how to manage your projects with uv, please refer to their `project guide <https://docs.astral.sh/uv/guides/projects/>`_ and their `project reference page <https://docs.astral.sh/uv/concepts/projects/>`_.

3. Run your scripts with uv
---------------------------

Once your project is set, you can run any scripts from system terminal inside the project folder with **appLP** dependency using a simple command:

.. code-block:: shell

   uv run my_script.py

For more information on script dependencies with uv, please refer to their `script guide <https://docs.astral.sh/uv/guides/scripts/>`_.

Some scripts may be provided with the library :doc:`(see Reference Guide) <scripts>`.
To use them, you can just download them from the `GitHub repository <https://github.com/LancelotPincet/appLP/tree/main/src/applp/scripts>`_.

4. Run your script from an editor
---------------------------------

In practice, python scripts are often launched from an editor. Here are the following protocoles for most commonly used editors.

Visual Studio Code
~~~~~~~~~~~~~~~~~~

The console in **Visual Studio Code** (or any wrapper editor like **Cursor**) is a system terminal, so if you installed *uv* as suggested, you can just use :

.. code-block:: shell

   uv run my_script.py

**Visual Studio Code** also proposes a *Python extension* to give the ability to run scripts via a button (IPython under the hood).
If you use this button, do not forget to activate the *.venv* environment created (it may activate automatically if you run from project path, but this is not very consistent).
To manually activate : ``Ctrl+Shift+P → Python: Select Interpreter`` and select ``./.venv/Scripts/python.exe``

Anaconda tools (Spyder and Jupyter)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are using *Anaconda*, you probably are coding via *Spyder* and *Jupyter*. By default, these use the *root environment* of Anaconda with lots of packages pre-included (but not *appLP*!).

The **first option** is to manually launch a kernel with the *.venv* we created before on your *Anaconda Spyder/Jupyter*.

- Spyder: ``Preferences → Python Interpreter`` and select ``./.venv/Scripts/python.exe``
- Jupyter: ``ipykernel`` must be installed in *.venv* (``uv add jupyter ipykernel``), then ``Kernel → Change Kernel``
This first option can be tedious every day.

The **second option** is to install Spyder and Jupyter in the *.venv*.

.. code-block:: shell

   uv add jupyter ipykernel
   uv add spyder

Then you can call these in a terminal to open directly the softwares with the *.venv*
However installing *Spyder* with *uv* (= *pip* installation) can sometimes be difficult with dependencies.

Other editors
~~~~~~~~~~~~~

As other editors have not been tested, please refer to dedicated support to run scripts from virtual environments with these.

5. Get source code
------------------

If you want to use the source code locally to modify the library, you can `git clone` the `GitHub source code <https://github.com/LancelotPincet/appLP>`_.

First you need to have `git <https://git-scm.com/downloads>`_ installed on your computer. 
Go to the local directory where you want to save the repository (change ``PATH_TO_REPO_PARENT``):

.. code-block:: shell

   cd PATH_TO_REPO_PARENT

Then clone the repository:

.. code-block:: shell

   git clone https://github.com/LancelotPincet/appLP.git

Now the library source code should be present

If you want to contribute, you can do a pull-request in the GitHub repository.