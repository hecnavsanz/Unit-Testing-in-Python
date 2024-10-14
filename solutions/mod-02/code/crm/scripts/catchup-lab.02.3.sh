#!/usr/bin/env bash

# move to the crm project directory
cd "$HOME"/crm || exit
pwd
ls -l ./*

# 1. Skipping a test

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.3_1.a_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest -rps

# 2. Skipping a test when a condition is evaluated

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.3_2.a_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest -rs

# 3. Expecting a test to fail

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.3_3.a_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest -rxs

cp /solutions/mod-02/code/crm/src/controllers/lab_02.3_3.c_customer.py \
    "$HOME"/crm/src/controllers/customer.py
bat --pager=never "$HOME"/crm/src/controllers/customer.py

pytest -v -rxs

# 4. Using test data

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.3_4.a_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest -v

# 5. Using custom marks

cp /solutions/mod-02/code/crm/config/lab_02.3_5.a_pyproject.toml \
    "$HOME"/crm/pyproject.toml
bat --pager=never "$HOME"/crm/pyproject.toml

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.3_5.b_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest -rsxp -m modify

pytest -rsxp -m query

pytest --markers

# 6. Using custom marks in parametrized tests

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.3_6.a_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest -rsxp -m query -m not_a_customer

cp /solutions/mod-02/code/crm/config/lab_02.3_6.c_pyproject.toml \
    "$HOME"/crm/pyproject.toml
bat --pager=never "$HOME"/crm/pyproject.toml

pytest -rsxp -m query -m not_a_customer

cd "$HOME" || exit
