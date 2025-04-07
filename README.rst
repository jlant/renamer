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

You can also run the command line interface with:

.. code:: bash

   python -m renamer --help

Library
~~~~~~~
The Python package can be used as a library:

.. code:: python

   >>> from renamer import renamer
   >>> text = """
   ... "You have power over your mind, not outside events.
   ... Realize this, and you will find strength." by Marcus Aurelius
   ... """
   >>> renamer.count_words(text)
   >>> {'You': 1, 'have': 1, 'power': 1, 'over': 1, 'your': 1, 'mind': 1, 'not': 1, 'outside': 1, 'events': 1, 'Realize': 1, 'this': 1, 'and': 1, 'you': 1, 'will': 1, 'find': 1, 'strength': 1, 'by': 1, 'Marcus': 1, 'Aurelius': 1}


Authors
-------

Development Lead
~~~~~~~~~~~~~~~~
* Jeremiah Lant, jeremiahlant@gmail.com

Contributors
~~~~~~~~~~~~
*
