# conftest.py configuration file
from models.customer import Customer
import pytest


@pytest.fixture(scope="package")
def a_customer():
    return Customer(1, "John Doe", "john.doe@labs.io", "1234567890")

@pytest.fixture(scope="package")
def another_customer():
    return Customer(2, "Jane Smith", "jane.smith@labs.io", "9876543210")

@pytest.fixture(scope="package")
def some_customers(a_customer, another_customer):
    return [a_customer, another_customer]

