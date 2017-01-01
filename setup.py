# -*- coding: utf-8 -*-
"""
github.com/LinxiFan/Stanford-theme
"""
from setuptools import setup
from stanford_theme import __version__


setup(
    name='stanford_theme',
    version=__version__,
    url='https://github.com/LinxiFan/Stanford-theme/',
    license='MIT',
    author='Linxi (Jim) Fan',
    author_email='jimfan@cs.stanford.edu',
    description='Stanford theme for Sphinx documentation generator and ReadTheDoc.org',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['stanford_theme'],
    package_data={'stanford_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
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
