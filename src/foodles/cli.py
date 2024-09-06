"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m foodles` python will execute
    ``__main__.py`` as a script. That means there will not be any
    ``foodles.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there"s no ``foodles.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""

import argparse

from .core import word_frequency

parser = argparse.ArgumentParser(
    description="Displays the n most frequent words in a sentence."
)
parser.add_argument("sentence", type=str, help="The sentence containing the words.")
parser.add_argument("n", type=int, help="The number of frequent words to display.")


def run():
    args = parser.parse_args()
    print(word_frequency(args.sentence, args.n))
    parser.exit(0)
