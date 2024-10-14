# -*- coding: utf-8 -*-
# test the customer controller
from controllers.customer import CustomerController
from models.customer_exception import CustomerNotFoundException
from utils.file_storage import FileStorage
import pytest


class TestCustomerController:

    # initialize the customer database
    @pytest.fixture(scope="class")
    def database(self):
        return FileStorage()

    # load customers into the customer database
    @pytest.fixture(scope="class")
    def customers_database(self, database, some_customers):
        for customer in some_customers:
            database.write(customer)
        yield database
        database.cleanup()

    # test the add method
    @pytest.mark.modify
    def test_add(self, customers_database, not_a_customer):
        controller = CustomerController(customers_database)

        assert customers_database.read_by_key("cust_id", not_a_customer.get_id()) is None, \
            "Customer already exists"
        assert (controller.add(not_a_customer) ==
                customers_database.read_by_key("cust_id", not_a_customer.get_id())), "Customer not added"

    # test the remove method
    @pytest.mark.modify
    def test_remove(self, customers_database, another_customer):
        controller = CustomerController(customers_database)

        assert controller.remove(another_customer) != customers_database.read_by_key("cust_id",
                                                                                     another_customer.get_id()), \
            "Customer not removed"

    # test the modify method
    @pytest.mark.modify
    def test_change(self, customers_database, another_customer, not_a_customer):
        controller = CustomerController(customers_database)
        idn_an = another_customer.get_id()
        idn_nan = not_a_customer.get_id()

        assert (controller.change(not_a_customer, another_customer) ==
                customers_database.read_by_key("cust_id", idn_an)), "Customer not modified"
        assert customers_database.read_by_key("cust_id", idn_nan) is None, "Customer still exists"

    # test the get all method
    @pytest.mark.query
    def test_get_all(self, customers_database):
        controller = CustomerController(customers_database)

        assert controller.get_all() == customers_database.read_all(), "Customers not found"

    # test the get by id method
    @pytest.mark.query
    def test_get_by_id(self, customers_database, a_customer):
        controller = CustomerController(customers_database)
        idn = a_customer.get_id()

        assert controller.get_by_id(idn) == a_customer, \
            "Customer not found"

        with pytest.raises(CustomerNotFoundException) as e:
            controller.get_by_id(3) == a_customer
        assert "Customer not found" in str(e.value), "No CustomerNotFoundException raised"

    # test the get by email method
    @pytest.mark.query
    def test_get_by_email(self, customers_database, a_customer):
        controller = CustomerController(customers_database)
        email = a_customer.get_email()

        assert controller.get_by_email(email) == a_customer, "Customer not found"

        with pytest.raises(CustomerNotFoundException) as e:
            controller.get_by_email("joe.fresh@labs.io") == a_customer
        assert "Customer not found" in str(e.value), "No CustomerNotFoundException raised"
