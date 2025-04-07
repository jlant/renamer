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
     --pattern TEXT      A pattern to apply when renaming with the following
                         placeholders: {index}, {original_name}, {date}
     --prefix TEXT       A prefix to add to a new file name.
     --date-format TEXT  A date format to use with the {date} placeholder.
                         (default: %Y-%m-%d)
     --dry_run           A flag to show what the renaming result would be.
                         (default: False)
     --version           Show the version and exit.
     --help              Show this message and exit.

You can also run the command line interface with:

.. code:: bash

   python -m renamer --help

Examples
~~~~~~~~
Add a prefix to files in the directory `tests/test_files`:

.. code:: bash

   renamer --prefix="new_" tests/test_files/

Add a pattern using built-in placeholders `{index}`, `{original_name}`, and `{date}`:

.. code:: bash

   renamer --pattern="{index}_{original_name}_{date}" tests/test_files

Use the `--dry_run` flag to show the renaming result before renaming the files:

.. code:: bash

   $ renamer --prefix="new_" --pattern="{original_name}_{date}" --dry_run tests/test_files/
   [Dry run] Would rename: file_a.txt -> new_file_a_2025-04-07.txt
   [Dry run] Would rename: file_b.txt -> new_file_b_2025-04-07.txt
   [Dry run] Would rename: file_c.txt -> new_file_c_2025-04-07.txt

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
* Jeremiah Lant, jeremiahlant@gmail.com
