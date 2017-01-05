Stanford theme for Sphinx
=========================

Modification
------------

Design
~~~~~~

Online demo of the theme:
`linxifan.github.io/Sphinx-demo/ <https://linxifan.github.io/Sphinx-demo/>`__

Stanford web color specification:
`[1] <https://identity.stanford.edu/overview/color.html>`__ and
`[2] <https://identity.stanford.edu/web-toolkit/color.html>`__

Add new fonts
~~~~~~~~~~~~~

1. Edit ``bower.json``, add ``ubuntumono-googlefont`` to dependency
   list.
2. Edit ``Gruntfile.js``, add font paths like the others.
3. Edit ``sass/_theme_font_local.sass``, note that ``font-weight: 400``
   corresponds to normal font while ``700`` correspoonds to bold.
4. Make sure the font files are copied to
   ``sphinx_theme/<mytheme>/static/fonts/``

SASS
~~~~

-  ``bower_components/wyrm`` contains the SASS for the original WYRM
   core. You can override variables in it to use customized color.
-  ``sass/_theme_variables.sass`` defines most of the colors.
-  ``sass/_theme_rst.sass`` defines how to render any reStructuredText
   file. All customizations are marked with ``mydef`` in the code
   comment.
-  ``sass/_theme_layout.css`` defines how to render menu, navigation
   bars, etc.

Workflow
~~~~~~~~

1. Work in ``sass/`` folder and Grunt will auto copy the generated files
   into ``test_theme``
2. Once done, copy ``sass/`` to ``sass_<newtheme>`` and copy
   ``test_theme`` to ``sphinx_theme/<newtheme>`` subdir.
3. Update ``sphinx_theme/__init__.py`` to include the new theme.

Installation
------------

Via package
~~~~~~~~~~~

Download the package or add it to your ``requirements.txt`` file:

.. code:: bash

    $ pip install sphinx_theme

In your ``conf.py`` file:

.. code:: python

    import sphinx_theme
    html_theme = "stanford_theme"
    html_theme_path = [sphinx_theme.get_html_theme_path('stanford-theme')]

    # All available themes:
    print(sphinx_theme.THEME_LIST)
    # >> ['stanford_theme', 'neo_rtd_theme']

Via git or download
~~~~~~~~~~~~~~~~~~~

Symlink or subtree the ``sphinx_theme/sphinx_theme`` repository into
your documentation at ``docs/_themes/sphinx_theme`` then add the
following two settings to your Sphinx conf.py file:

.. code:: python

    html_theme = "stanford_theme"
    html_theme_path = ["_themes/sphinx_theme", ]

Configuration
-------------

You can configure different parts of the theme.

Project-wide configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

The theme's project-wide options are defined in the
``sphinx_theme/<mytheme>/theme.conf`` file of this repository, and can
be defined in your project's ``conf.py`` via ``html_theme_options``. For
example:

.. code:: python

    html_theme_options = {
        'collapse_navigation': False,
        'display_version': False,
        'navigation_depth': 3,
    }

Page-level configuration
~~~~~~~~~~~~~~~~~~~~~~~~

Pages support metadata that changes how the theme renders. You can
currently add the following:

-  ``:github_url:`` This will force the "Edit on GitHub" to the
   configured URL
-  ``:bitbucket_url:`` This will force the "Edit on Bitbucket" to the
   configured URL
-  ``:gitlab_url:`` This will force the "Edit on GitLab" to the
   configured URL

How the Table of Contents builds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently the left menu will build based upon any ``toctree(s)`` defined
in your index.rst file. It outputs 2 levels of depth, which should give
your visitors a high level of access to your docs. If no toctrees are
set the theme reverts to sphinx's usual local toctree.

It's important to note that if you don't follow the same styling for
your rST headers across your documents, the toctree will misbuild, and
the resulting menu might not show the correct depth when it renders.

Also note that the table of contents is set with ``includehidden=true``.
This allows you to set a hidden toc in your index file with the
`hidden <http://sphinx-doc.org/markup/toctree.html>`__ property that
will allow you to build a toc without it rendering in your index.

By default, the navigation will "stick" to the screen as you scroll.
However if your toc is vertically too large, it will revert to static
positioning. To disable the sticky nav altogether change the setting in
``conf.py``.

Make the theme compatible with ReadTheDocs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently if you import stanford\_theme in your local sphinx build, then
pass that same config to Read the Docs, it will fail, since RTD gets
confused. If you want to run this theme locally and then also have it
build on RTD, then you can add something like this to your config.
Thanks to Daniel Oaks for this.

.. code:: python

    # on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

    if not on_rtd:  # only import and set the theme if we're building docs locally
        import sphinx_theme
        html_theme = 'stanford_theme'
        html_theme_path = [sphinx_theme.get_html_theme_path('stanford_theme')]

    # otherwise, readthedocs.org uses their theme by default, so no need to specify it

Editing the theme
-----------------

The theme is primarily a `sass <http://www.sass-lang.com>`__ project
that requires a few other sass libraries. I'm using
`bower <http://www.bower.io>`__ to manage these dependencies and
`sass <http://www.sass-lang.com>`__ to build the css. The good news is I
have a very nice set of `grunt <http://www.gruntjs.com>`__ operations
that will not only load these dependencies, but watch for changes,
rebuild the sphinx demo docs and build a distributable version of the
theme. The bad news is this means you'll need to set up your environment
similar to that of a front-end developer (vs. that of a python
developer). That means installing node and ruby.

Set up your environment
~~~~~~~~~~~~~~~~~~~~~~~

1. Install `sphinx <http://www.sphinx-doc.org>`__ into a virtual
   environment.

::

    pip install sphinx

2. Install sass

::

    gem install sass

2. Install node, bower and grunt.

::

    // Install node
    brew install node

    // Install bower and grunt
    npm install -g bower grunt-cli

    // Now that everything is installed, let's install the theme dependecies.
    npm install

Now that our environment is set up, make sure you're in your virtual
environment, go to this repository in your terminal and run grunt:

::

    grunt

This default task will do the following **very cool things that make it
worth the trouble**.

1. It'll install and update any bower dependencies.
2. It'll run sphinx and build new docs.
3. It'll watch for changes to the sass files and build css from the
   changes.
4. It'll rebuild the sphinx docs anytime it notices a change to .rst,
   .html, .js or .css files.
