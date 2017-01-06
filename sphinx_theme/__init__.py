"""
Stanford ReadTheDocs theme for Sphinx documentation generator. 
"""
import os

__version__ = '1.0'
__version_full__ = __version__


THEME_LIST = ['stanford_theme', 'neo_rtd_theme']


def get_html_theme_path(theme='stanford_theme'):
    """Return list of HTML theme paths."""
    theme = theme.replace('-', '_')
    if not theme in THEME_LIST:
        raise ValueError('{} not found: available themes are {}.'.format(theme, THEME_LIST))

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return cur_dir
