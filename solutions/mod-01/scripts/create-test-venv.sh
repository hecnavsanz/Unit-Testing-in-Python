#!/usr/bin/env bash

# cleanup the virtual environment
rm -Rf "$HOME"/test-venv

# create a new virtual environment and activate it
virtualenv --prompt test "$HOME"/test-venv
. "$HOME"/test-venv/bin/activate

# upgrade pip
pip install --upgrade pip

# install the required packages
pip install -r /solutions/mod-01/requirements/pytest.txt

# list the pytest package information
pip show pytest

pytest --version
