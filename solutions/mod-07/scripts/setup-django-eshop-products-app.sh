#!/usr/bin/env bash

. "$HOME"/test-venv/bin/activate

cd "$HOME"/online-store

python manage.py startapp products

ls -l products/*

# - __init__.py: empty file that tells Python that this directory should be considered a Python package.
# - admin.py: configuration for the Django admin site.
# - apps.py: configuration for the application.
# - models.py: the database schema (models) for the application.
# - tests.py: test cases for the application.
# - views.py: the views for the application.

