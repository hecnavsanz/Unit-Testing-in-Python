#!/usr/bin/env bash

CWD=$(pwd)

cd "$HOME"/crm-app

nohup flask run --host 0.0.0.0 --port 5000 > /tmp/flask_crm-app_output.log 2>&1 &

cd "$CWD"
