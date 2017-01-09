#!/bin/bash
cp -rf sass/* sass_$1/
cp -rf test_theme/static/* sphinx_theme/$1_theme/static/
cp -rf test_theme/*.html sphinx_theme/$1_theme/
