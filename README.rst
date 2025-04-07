renamer
=======

*Renamer is a tool that renames files in a directory based on a pattern along with other options.*


Installation
------------

Create a virtual environment

.. code:: bash

   python -m venv venv

Activate the virtual environment

.. code:: bash

   source venv/bin/activate

Install the Python package using ``pip`` with the ``pyproject.toml`` file in the current
working directory:

.. code:: bash

   python -m pip install .


Usage
-----

Command Line Interface (CLI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Python package has a command line interface with a help menu that shows how to use
the package from the command line:

.. code:: bash

   renamer --help
   Usage: renamer [OPTIONS] DIRECTORY

     Command line interface for renamer

     Renamer is a tool that renames files in a directory based on a pattern along
     with other options.

     DIRECTORY is the path to the directory containing the files to rename.

   Options:
     --pattern TEXT  A pattern to apply when renaming with the following
                     placeholders: {index}, {original_name}
     --prefix TEXT   A prefix to add to a new file name.
     --version       Show the version and exit.
     --help          Show this message and exit.

You can also run the command line interface with:

.. code:: bash

   python -m renamer --help

Examples
~~~~~~~~
Add a prefix to files in the directory `tests/test_files`:

.. code:: bash

   renamer --prefix="new_" tests/test_files/

Add a pattern using built-in placeholders `{index}` and `{original_name}`:

.. code:: bash

   renamer --pattern="{index}_{original_name}" tests/test_files

Library
~~~~~~~
The Python package can be used as a library:

.. code:: python

   >>> from renamer import renamer
   >>> test_directory = Path("tests/test_files").resolve()
   >>> pattern = "{index}_{original_name}_updated"
   >>> prefix = "new_"
   >>> rename_files(directory=test_directory, pattern=pattern, prefix=prefix)


Authors
-------

Development Lead
~~~~~~~~~~~~~~~~
* Jeremiah Lant, jeremiah.lant@samtec.com

Contributors
~~~~~~~~~~~~
*
