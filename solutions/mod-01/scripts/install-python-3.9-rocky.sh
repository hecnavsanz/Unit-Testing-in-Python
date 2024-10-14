#!/usr/bin/env bash

sudo dnf install python3 -y

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo update-alternatives --remove python /usr/bin/python3.11

python /solutions/mod-01/config/get-pip.py

python -m pip install --user virtualenv

# python -V
# pip -V
# virtualenv --version
