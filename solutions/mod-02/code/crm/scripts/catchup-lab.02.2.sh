#!/usr/bin/env bash

# create crm project directories
rm -Rf "$HOME"/crm
mkdir -p "$HOME"/crm
mkdir -p "$HOME"/crm/src/models
mkdir -p "$HOME"/crm/src/controllers
mkdir -p "$HOME"/crm/tests/models
mkdir -p "$HOME"/crm/tests/controllers
cd "$HOME"/crm || exit
pwd
ls -l ./*

# 1. Configure non-default naming conventions for Pytest directories and files

cp /solutions/mod-02/code/crm/src/models/__init__.py "$HOME"/crm/src/models/__init__.py
cp /solutions/mod-02/code/crm/src/models/lab_02.2_1.b_model.py "$HOME"/crm/src/models/model.py
cp /solutions/mod-02/code/crm/src/models/lab_02.2_1.b_customer.py "$HOME"/crm/src/models/customer.py
cp /solutions/mod-02/code/crm/src/controllers/__init__.py "$HOME"/crm/src/controllers/__init__.py
cp /solutions/mod-02/code/crm/src/controllers/lab_02.2_1.b_controller.py "$HOME"/crm/src/controllers/controller.py
cp /solutions/mod-02/code/crm/src/controllers/lab_02.2_1.b_customer.py "$HOME"/crm/src/controllers/customer.py
cp /solutions/mod-02/code/crm/src/lab_02.2_1.b_sample-customers.py "$HOME"/crm/src/sample-customers.py
bat --pager=never "$HOME"/crm/src/models/model.py
bat --pager=never "$HOME"/crm/src/models/customer.py
bat --pager=never "$HOME"/crm/src/controllers/controller.py
bat --pager=never "$HOME"/crm/src/controllers/customer.py
bat --pager=never "$HOME"/crm/src/sample-customers.py

python "$HOME"/crm/src/sample-customers.py

# 2. Assertions with custom messages

cp /solutions/mod-02/code/crm/config/lab_02.2_1.c_pyproject.toml "$HOME"/crm/pyproject.toml
cp /solutions/mod-02/code/crm/tests/controllers/lab_02.2_1.c_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/pyproject.toml
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest -v

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.2_2.b_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest tests/controllers/test_customer_controller.py::TestCustomerController::test_get_by_id

# 3. Modifying the assert statement to display a custom message when the assert fails

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.2_3.a_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest tests/controllers/test_customer_controller.py::TestCustomerController::test_get_by_id

# 4. Using the pytest_assertrepr_compare function in the conftest.py file
#    to display a custom message when the assert fails

cp /solutions/mod-02/code/crm/config/lab_02.2_4.a_conftest.py "$HOME"/crm/tests/conftest.py
bat --pager=never "$HOME"/crm/tests/conftest.py
cp /solutions/mod-02/code/crm/tests/controllers/lab_02.2_4.b_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest tests/controllers/test_customer_controller.py::TestCustomerController::test_get_by_id

# 5. Re-writing assertions in non-test modules

cp /solutions/mod-02/code/crm/src/models/lab_02.2_5.a_customer.py "$HOME"/crm/src/models/customer.py
bat --pager=never "$HOME"/crm/src/models/customer.py

pytest tests/controllers/test_customer_controller.py::TestCustomerController::test_get_by_id

cp /solutions/mod-02/code/crm/config/lab_02.2_5.c_conftest.py "$HOME"/crm/tests/conftest.py
bat --pager=never "$HOME"/crm/tests/conftest.py

pytest tests/controllers/test_customer_controller.py::TestCustomerController::test_get_by_id

# 6. Asserting exceptions

cp /solutions/mod-02/code/crm/src/models/lab_02.2_6.a_customer_exception.py "$HOME"/crm/src/models/customer_exception.py
cp /solutions/mod-02/code/crm/src/controllers/lab_02.2_6.a_customer.py "$HOME"/crm/src/controllers/customer.py
bat --pager=never "$HOME"/crm/src/models/customer_exception.py
bat --pager=never "$HOME"/crm/src/controllers/customer.py

cp /solutions/mod-02/code/crm/tests/controllers/lab_02.2_6.b_test_customer_controller.py \
    "$HOME"/crm/tests/controllers/test_customer_controller.py
bat --pager=never "$HOME"/crm/tests/controllers/test_customer_controller.py

pytest tests/controllers/test_customer_controller.py::TestCustomerController::test_get_by_id

cd "$HOME" || exit
