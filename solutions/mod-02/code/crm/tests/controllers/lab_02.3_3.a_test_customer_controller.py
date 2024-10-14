# -*- coding: utf-8 -*-
# test the customer controller
from controllers.customer import CustomerController
from models.customer import Customer
from models.customer_exception import CustomerNotFoundException
import pytest
import sys
import random


class TestCustomerController:

    # test the add method
    def test_add(self):
        controller = CustomerController()
        customer = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")

        assert controller.add(customer) == 1, "Customer not added"

    # test the remove method
    def test_remove(self):
        controller = CustomerController()
        customer = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        controller.add(customer)

        assert controller.remove(customer) == 1, "Customer not removed"

    # test the get all method
    @pytest.mark.skip(reason="CustomerController.get_all method not tested")
    def test_get_all(self):
        customers = [Customer(1, "John Doe", "john.doe@labs.io", "1234567890"),
                     Customer(2, "Jane Smith", "jane.smith@labs.io", "9876543210")]
        controller = CustomerController()
        for customer in customers:
            controller.add(customer)

        assert controller.get_all() == customers, "Customers not found"

    # test the get by id method
    def test_get_by_id(self):

        if sys.version_info >= (3, 11):
            pytest.skip("Requires Python 3.11 or higher")

        customers = [Customer(1, "John Doe", "john.doe@labs.io", "1234567890"),
                     Customer(2, "Jane Smith", "jane.smith@labs.io", "9876543210")]
        controller = CustomerController()
        for customer in customers:
            controller.add(customer)

        for i in range(1, len(customers)):
            assert controller.get_by_id(i) == customers[i-1], "Customer not found"

        with pytest.raises(CustomerNotFoundException) as e:
            controller.get_by_id(3) is None
        assert "Customer not found" in str(e.value), "No CustomerNotFoundException exception raised"

    # test the get by email method
    @pytest.mark.xfail(reason="CustomerController.get_by_email method not implemented", run=True)
    def test_get_by_email(self):
        controller = CustomerController()
        customers = [Customer(1, "John Doe", "john.doe@labs.io", "1234567890"),
                     Customer(2, "Jane Smith", "jane.smith@labs.io", "9876543210")]
        for customer in customers:
            controller.add(customer)
        rnd_customer = random.choice(customers)

        assert controller.get_by_email(rnd_customer.get_email()) == rnd_customer, "Customer not found"