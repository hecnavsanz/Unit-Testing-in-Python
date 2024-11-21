#!/usr/bin/env bash

# cleanup the virtual environment
rm -Rf "$HOME"/selenium-venv

# create a new virtual environment and activate it
virtualenv --prompt selenium-venv "$HOME"/selenium-venv
. "$HOME"/selenium-venv/bin/activate

# upgrade pip
pip install --upgrade pip

# install the required packages
pip install -r /solutions/mod-09/requirements/django-selenium-postgres.txt

# list the pytest package information
pip show pytest

pytest --version
