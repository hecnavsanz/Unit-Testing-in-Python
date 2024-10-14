#!/usr/bin/env bash

# cleanup the virtual environment
rm -Rf "$HOME"/selenium-venv

# create a new virtual environment and activate it
virtualenv --prompt selenium "$HOME"/selenium-venv
. "$HOME"/selenium-venv/bin/activate

# upgrade pip
pip install --upgrade pip

# install the required packages
pip install -r /solutions/mod-08/requirements/pytest-selenium.txt

# list the pytest and selenium packages information
pip show pytest selenium

pytest --version
