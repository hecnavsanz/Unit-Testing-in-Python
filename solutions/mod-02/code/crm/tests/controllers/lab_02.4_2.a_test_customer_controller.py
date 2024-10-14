# -*- coding: utf-8 -*-
# test the customer controller
from controllers.customer import CustomerController
from models.customer import Customer
from models.customer_exception import CustomerNotFoundException
import pytest
import random


class TestCustomerController:

    @pytest.fixture
    def a_customer(self):
        """ returns a customer """
        return Customer(1, "John Doe", "john.doe@labs.io", "1234567890")

    @pytest.fixture
    def another_customer(self):
        """ returns another customer """
        return Customer(2, "Jane Smith", "jane.smith@labs.io", "9876543210")

    @pytest.fixture
    def some_customers(self, a_customer, another_customer):
        """ returns some customers """
        return [a_customer,
                another_customer]

    # test the add method
    @pytest.mark.modify
    def test_add(self, a_customer):
        controller = CustomerController()
        customer = a_customer
        idn = a_customer.get_id()

        assert controller.add(customer) == idn, "Customer not added"

    # test the remove method
    @pytest.mark.modify
    def test_remove(self, a_customer):
        controller = CustomerController()
        customer = a_customer
        idn = a_customer.get_id()
        controller.add(customer)

        assert controller.remove(customer) == idn, "Customer not removed"

    # test the get all method
    @pytest.mark.query
    def test_get_all(self, some_customers):
        controller = CustomerController()
        for customer in some_customers:
            controller.add(customer)

        assert controller.get_all() == some_customers, "Customers not found"

    # test the get by id method
    @pytest.mark.query
    def test_get_by_id(self, a_customer):
        controller = CustomerController()
        customer = a_customer
        idn = a_customer.get_id()
        controller.add(customer)

        assert controller.get_by_id(idn) == customer, "Customer not found"

        with pytest.raises(CustomerNotFoundException) as e:
            controller.get_by_id(3) == customer
        assert "Customer not found" in str(e.value), "No CustomerNotFoundException raised"

    # test the get by email method
    @pytest.mark.query
    def test_get_by_email(self, some_customers):
        controller = CustomerController()
        for customer in some_customers:
            controller.add(customer)
        rnd_customer = random.choice(some_customers)

        assert controller.get_by_email(rnd_customer.get_email()) == rnd_customer, "Customer not found"

        with pytest.raises(CustomerNotFoundException) as e:
            controller.get_by_email("joe.fresh@labs.io") == rnd_customer
        assert "Customer not found" in str(e.value), "No CustomerNotFoundException raised"
