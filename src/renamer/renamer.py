"""Main module for renamer

This is an example module with:
* a module level docstring showing `numpydoc <https://numpydoc.readthedocs.io/en/latest/format.html>`_ style
* an example function with a docstring and typing that counts the number of words from a text string
* a ``if __name__ == "__main__":`` block to define code that should only be executed
when the module is run directly, and not when it is imported

Notes
-----
Code documentation follows `numpydoc <https://numpydoc.readthedocs.io/en/latest/format.html>`_ style

See Also
--------
`numpydoc example.py <https://numpydoc.readthedocs.io/en/latest/example.html#example>`_


References
----------
Cite relevant references in this section.

Such as this recommended paper: `Best Practices in Scientific Computing`_.

.. _Best Practices in Scientific Computing: https://doi.org/10.1371/journal.pbio.1001745

"""
import string
from collections import Counter
from typing import Dict


def count_words(text: str) -> Dict[str, int]:
    """Count words in a given text string.

    Count the number of words in a given text string, and return a dictionary
    sorted by the number of words in descending order.

    Parameters
    ----------
    text : str
        The text string.

    Returns
    -------
    dict
        The sorted dictionary mapping of word to word count

    """
    words = text.split()
    words_generator_object = (word.strip(string.punctuation) for word in words)
    words_counter = Counter(words_generator_object)
    words_dict = dict(words_counter)
    words_dict_sorted = dict(
            sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
    )

    return words_dict_sorted


def main():
    """Main function.

    Output the count of words in a text string.
    """
    text = """
    "You have power over your mind, not outside events.
    Realize this, and you will find strength." by Marcus Aurelius
    """
    words_dict = count_words(text)
    output = "\n".join([f"{key} {value}" for key, value in words_dict.items()])
    print(output)


if __name__ == "__main__":
    main()

