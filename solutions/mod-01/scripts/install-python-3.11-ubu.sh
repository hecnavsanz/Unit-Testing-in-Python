#!/usr/bin/env bash

sudo apt install python3.11 -y

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1
sudo update-alternatives --remove python /usr/bin/python3.10

python /solutions/mod-01/config/get-pip.py

python -m pip install --user virtualenv

# python -V
# pip -V
# virtualenv --version
