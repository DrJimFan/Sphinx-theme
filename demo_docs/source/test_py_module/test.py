# -*- coding: utf-8 -*-
"""Test Module for sphinx_rtd_theme."""

def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.
    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
      big_table (int): An open Bigtable Table instance.
      keys (str): A sequence of strings representing the key of each table row to fetch.
      other_silly_variable (float): Another optional :math:`\\mu^\\frac{\\theta}{3}`

    Returns:
      A dict mapping keys to the corresponding table row data
      fetched. Each row is represented as a tuple of strings. For
      example:

      .. math::
         (a + b)^2 &= a^2 + 2ab + b^2 \\\\
                  &= \\sum_{i=0}^{\\infty} f(x) dx

         (a - b)^1 = a^2 - 2ab + b^2

      If a key from the keys argument is missing from the dictionary,
      then that row was not found in the table.

    Raises:
      IOError: An error occurred accessing the bigtable.Table object.
    """
    pass


def seonc_method(x, y, *z):
    """Computes shit
    Randoms hit y aefiojo dgj

    Args:
      X: An open wyine fking page
      Y: A sequence of strings representing the key of each table row
        to fetch.
      Z: Another optional variable, that has a much
        longer name than the other args, and which does nothing.

    Returns:
      Bro's algorithm.

      .. code:: python

        if i > 0:
            with AiChan() as ai:
                print(i, ai, **kwargs)

      If a key from the keys argument is missing from the dictionary,
      then that row was not found in the table.

    Raises:
      IOError: An error occurred accessing the bigtable.Table object.
    """
    pass


class Foo:

    r"""Docstring for class Foo.

    This text tests for the formatting of docstrings generated from output
    ``sphinx.ext.autodoc``. Which contain reST, but sphinx nests it in the
    ``<dl>``, and ``<dt>`` tags. Also, ``<tt>`` is used for class, method names
    and etc, but those will *always* have the ``.descname`` or
    ``.descclassname`` class.

    Normal ``<tt>`` (like the <tt> I just wrote here) needs to be shown with
    the same style as anything else with ````this type of markup````.

    It's common for programmers to give a code example inside of their
    docstring::

        from test_py_module import Foo

        myclass = Foo()
        myclass.dothismethod('with this argument')
        myclass.flush()

        print(myclass)


    Here is a link to :py:meth:`capitalize`.
    Here is a link to :py:meth:`__init__`.

    """

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1

    flox = 1.5   #: Doc comment for Foo.flox. One line only.

    baz = 2
    """Docstring for class attribute Foo.baz."""

    def __init__(self, qux, spam=False):
        """Start the Foo.

        :param qux: The first argument to initialize class.
        :type qux: string
        :param spam: Spam me yes or no...
        :type spam: bool

        """
        #: Doc comment for instance attribute qux.
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam."""

    def add(self, val1, val2):
        """Return the added values.

        :param val1: First number to add.
        :type val1: int
        :param val2: Second number to add.
        :type val2: int
        :rtype: int

        """

        return val1 + val2

    def capitalize(self, myvalue):
        """Return a string as uppercase.

        :param myvalue: String to change
        :type myvalue: string
        :rtype: string

        """

        return myvalue.upper()

    def another_function(self, a, b, **kwargs):
        """
        Here is another function.

        :param a: The number of green hats you own.
        :type a: int

        :param b: The number of non-green hats you own.
        :type b: int

        :param kwargs: Additional keyword arguments. Each keyword parameter
                       should specify the name of your favorite cuisine.
                       The values should be floats, specifying the mean price
                       of your favorite dish in that cooking style.
        :type kwargs: float

        :returns: A 2-tuple.  The first element is the mean price of all dishes
                  across cuisines.  The second element is the total number of
                  hats you own: :math:`a + b`.
        :rtype: tuple

        :raises ValueError: When ``a`` is not an integer.

        """
        return sum(kwargs.values()) / len(kwargs), a + b
