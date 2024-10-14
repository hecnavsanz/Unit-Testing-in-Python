# conftest.py configuration file
from models.customer import Customer
import pytest


@pytest.fixture(scope="module")
def a_customer():
    return Customer(1, "John Doe", "john.doe@labs.io", "1234567890")

@pytest.fixture(scope="module")
def another_customer():
    return Customer(2, "Jane Smith", "jane.smith@labs.io", "9876543210")

@pytest.fixture(scope="module")
def not_a_customer():
    return Customer(3, "Joe Fresh", "joe.fresh@labs.io", "1234554321")

@pytest.fixture(scope="module")
def some_customers(a_customer, another_customer):
    return [a_customer, another_customer]
