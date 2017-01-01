Stanford theme for Sphinx 
==========================

## Add new fonts

- Edit `bower.json` 

ReadTheDoc theme
==========================

View a working [demo](http://docs.readthedocs.org) over on
[readthedocs.org](http://www.readthedocs.org).

This is a mobile-friendly [sphinx](http://www.sphinx-doc.org) theme I
made for [readthedocs.org](http://www.readthedocs.org). It's currently
in development there and includes some rtd variable checks that can be
ignored if you're just trying to use it on your project outside of that
site.

**This repo also exists as a submodule within the readthedocs itself**,
so please make your edits to the SASS files here, rather than the .css
files on RTD.

Installation
------------

### Via package

Download the package or add it to your `requirements.txt` file:

```bash
$ pip install sphinx_rtd_theme
```

In your `conf.py` file:

```python
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

### Via git or download

Symlink or subtree the `sphinx_rtd_theme/sphinx_rtd_theme` repository
into your documentation at `docs/_themes/sphinx_rtd_theme` then add the
following two settings to your Sphinx conf.py file:

``` {.sourceCode .python}
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]
```

Configuration
-------------

You can configure different parts of the theme.

### Project-wide configuration

The theme's project-wide options are defined in the
`sphinx_rtd_theme/theme.conf` file of this repository, and can be
defined in your project's `conf.py` via `html_theme_options`. For
example:

```python 
html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
    'navigation_depth': 3,
}
```

### Page-level configuration

Pages support metadata that changes how the theme renders. You can
currently add the following:

-   `:github_url:` This will force the "Edit on GitHub" to the
    configured URL
-   `:bitbucket_url:` This will force the "Edit on Bitbucket" to the
    configured URL
-   `:gitlab_url:` This will force the "Edit on GitLab" to the
    configured URL

How the Table of Contents builds
--------------------------------

Currently the left menu will build based upon any `toctree(s)` defined
in your index.rst file. It outputs 2 levels of depth, which should give
your visitors a high level of access to your docs. If no toctrees are
set the theme reverts to sphinx's usual local toctree.

It's important to note that if you don't follow the same styling for
your rST headers across your documents, the toctree will misbuild, and
the resulting menu might not show the correct depth when it renders.

Also note that the table of contents is set with `includehidden=true`.
This allows you to set a hidden toc in your index file with the
[hidden](http://sphinx-doc.org/markup/toctree.html) property that will
allow you to build a toc without it rendering in your index.

By default, the navigation will "stick" to the screen as you scroll.
However if your toc is vertically too large, it will revert to static
positioning. To disable the sticky nav altogether change the setting in
`conf.py`.

Contributing or modifying the theme
-----------------------------------

The sphinx\_rtd\_theme is primarily a [sass](http://www.sass-lang.com)
project that requires a few other sass libraries. I'm using
[bower](http://www.bower.io) to manage these dependencies and
[sass](http://www.sass-lang.com) to build the css. The good news is I
have a very nice set of [grunt](http://www.gruntjs.com) operations that
will not only load these dependencies, but watch for changes, rebuild
the sphinx demo docs and build a distributable version of the theme. The
bad news is this means you'll need to set up your environment similar to
that of a front-end developer (vs. that of a python developer). That
means installing node and ruby.

### Set up your environment

1.  Install [sphinx](http://www.sphinx-doc.org) into a virtual
    environment.

```
pip install sphinx
```

2.  Install sass

```
gem install sass
```

2.  Install node, bower and grunt.

```
// Install node
brew install node

// Install bower and grunt
npm install -g bower grunt-cli

// Now that everything is installed, let's install the theme dependecies.
npm install
```

Now that our environment is set up, make sure you're in your virtual
environment, go to this repository in your terminal and run grunt:

```
grunt
```

This default task will do the following **very cool things that make it
worth the trouble**.

1.  It'll install and update any bower dependencies.
2.  It'll run sphinx and build new docs.
3.  It'll watch for changes to the sass files and build css from the
    changes.
4.  It'll rebuild the sphinx docs anytime it notices a change to .rst,
    .html, .js or .css files.


Using this theme locally, then building on Read the Docs?
---------------------------------------------------------

Currently if you import sphinx\_rtd\_theme in your local sphinx build,
then pass that same config to Read the Docs, it will fail, since RTD
gets confused. If you want to run this theme locally and then also have
it build on RTD, then you can add something like this to your config.
Thanks to Daniel Oaks for this.

```python
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify it
```
