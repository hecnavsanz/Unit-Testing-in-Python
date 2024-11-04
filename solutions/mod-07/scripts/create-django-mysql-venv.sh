#!/usr/bin/env bash

virtualenv --prompt django-venv django-venv

. django-venv/bin/activate

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config -y

pip install -r /solutions/mod-07/requirements/django-mysql.txt
