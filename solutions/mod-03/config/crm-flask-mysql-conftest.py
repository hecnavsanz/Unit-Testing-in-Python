# conftest.py configuration file
from models.customer import Customer
import pytest


@pytest.fixture(scope="package")
def cust_1():
    return Customer(1, "John Doe", "john.doe@labs.io", "(123) 456-7890")

@pytest.fixture(scope="package")
def cust_2():
    return Customer(2, "Jane Smith", "jane.smith@labs.io", "(987) 654-3210")

@pytest.fixture(scope="package")
def cust_3():
    return Customer(3, "Joe Fresh", "joe.fresh@labs.io", "(123) 455-4321")

@pytest.fixture(scope="package")
def cust_4():
    return Customer(4, "Michael Bloggs", "michael.bloggs@labs.io", "(555) 555-5555")

@pytest.fixture(scope="package")
def cust_1_upd():
    return Customer(1, "John Doe", "john.doe@labs.io", "(100) 200-3000")

@pytest.fixture(scope="package")
def cust_2_upd():
    return Customer(2, "Jane Smith", "jane.smith@labs.io", "(100) 200-3000")

@pytest.fixture(scope="package")
def cust_1_copy():
    return Customer(1, "John Doe", "john.doe@labs.io", "(123) 456-7890")

@pytest.fixture(scope="package")
def custs(cust_1, cust_2, cust_3):
    return [cust_1, cust_2, cust_3]

@pytest.fixture(scope="package")
def custs_after(cust_2_upd, cust_3, cust_4):
    return [cust_2_upd, cust_3, cust_4]
