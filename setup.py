# -*- coding: utf-8 -*-
"""
github.com/LinxiFan/Sphinx-theme
"""
from setuptools import setup
from sphinx_theme import __version__


setup(
    name='sphinx_theme',
    version=__version__,
    url='https://github.com/LinxiFan/Sphinx-theme/',
    license='MIT',
    author='Linxi (Jim) Fan',
    author_email='jimfan@cs.stanford.edu',
    description='Sphinx documentation theme based on readthedocs.org',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx_theme'],
   #package_data={'sphinx_theme': [
   #    'theme.conf',
   #    '*.html',
   #    'static/css/*.css',
   #    'static/js/*.js',
   #    'static/font/*.*'
   #]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
