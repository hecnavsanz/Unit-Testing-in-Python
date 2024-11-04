#!/usr/bin/env bash

. "$HOME"/test-venv/bin/activate

pip install --upgrade pip
python -m pip install Django

pip show django
python -m django --version

django-admin startproject eshop online-store

ls -l "$HOME"/online-store/*

# - manage.py: cmd-line utility that lets you interact with this Django project in various ways.
# - eshop/: directory that is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. eshop.urls).
#    * __init__.py: empty file that tells Python that this directory should be considered a Python package.
#    * settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
#    * urls.py: URL declarations for this Django project; a “table of contents” of your Django-powered site.
#    * asgi.py: entry-point for ASGI-compatible web servers to serve your project.
#    * wsgi.py: entry-point for WSGI-compatible web servers to serve your project.

cd "$HOME"/online-store
nohup python manage.py runserver 0.0.0.0:5000 &

curl -I http://localhost:5000

pkill --signal SIGTERM "python"

#python manage.py --help
#
#Type 'manage.py help <subcommand>' for help on a specific subcommand.
#
#Available subcommands:
#
#[auth]
#    changepassword
#    createsuperuser
#
#[contenttypes]
#    remove_stale_contenttypes
#
#[django]
#    check
#    compilemessages
#    createcachetable
#    dbshell
#    diffsettings
#    dumpdata
#    flush
#    inspectdb
#    loaddata
#    makemessages
#    makemigrations
#    migrate
#    optimizemigration
#    sendtestemail
#    shell
#    showmigrations
#    sqlflush
#    sqlmigrate
#    sqlsequencereset
#    squashmigrations
#    startapp
#    startproject
#    test
#    testserver
#
#[sessions]
#    clearsessions
#
#[staticfiles]
#    collectstatic
#    findstatic
#    runserver


#python manage.py runserver --help
#usage: manage.py runserver [-h] [--ipv6] [--nothreading] [--noreload] [--nostatic] [--insecure] [--version] [--settings SETTINGS] [--pythonpath PYTHONPATH] [--no-color] [--force-color] [--skip-checks] [addrport]
#
#Starts a lightweight web server for development and also serves static files.
#
#positional arguments:
#  addrport              Optional port number, or ipaddr:port
#
#options:
#  -h, --help            show this help message and exit
#  --ipv6, -6            Tells Django to use an IPv6 address.
#  --nothreading         Tells Django to NOT use threading.
#  --noreload            Tells Django to NOT use the auto-reloader.
#  --nostatic            Tells Django to NOT automatically serve static files at STATIC_URL.
#  --insecure            Allows serving static files even if DEBUG is False.
#  --version             Show program's version number and exit.
#  --settings SETTINGS   The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the DJANGO_SETTINGS_MODULE environment variable will be used.
#  --pythonpath PYTHONPATH
#                        A directory to add to the Python path, e.g. "/home/djangoprojects/myproject".
#  --no-color            Don't colorize the command output.
#  --force-color         Force colorization of the command output.
#  --skip-checks         Skip system checks.
