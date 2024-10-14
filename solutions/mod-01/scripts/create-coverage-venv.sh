#!/usr/bin/env bash

# cleanup the virtual environment
rm -Rf "$HOME"/coverage-venv

# create a new virtual environment and activate it
virtualenv --prompt coverage "$HOME"/coverage-venv
source "$HOME"/coverage-venv/bin/activate

# upgrade pip
pip install --upgrade pip

# install the required packages
pip install -r /solutions/mod-01/requirements/pytest-coverage.txt

# list the pytest and coverage packages information
pip show pytest coverage

pytest --version
coverage --version
