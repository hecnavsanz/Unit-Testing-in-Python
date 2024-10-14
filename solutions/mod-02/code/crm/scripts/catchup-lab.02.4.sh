#!/usr/bin/env bash

# move to the crm project directory
cd "$HOME"/crm || exit
pwd
ls -l ./*

# 1. Using fixtures

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.4_1.a_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest -rps

pytest --fixtures

pytest --fixtures-per-test

# 2. Nesting fixtures

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.4_2.a_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest -rps



cd "$HOME" || exit
