# -*- coding: utf-8 -*-
# test the customer controller
from controllers.customer import CustomerController
from models.customer import Customer


class TestCustomerController:

    # test the add method
    def test_add(self):
        controller = CustomerController()
        customer = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")

        assert controller.add(customer) == 1

    # test the remove method
    def test_remove(self):
        controller = CustomerController()
        customer = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        controller.add(customer)

        assert controller.remove(customer) == 1

    # test the get all method
    def test_get_all(self):
        customers = [Customer(1, "John Doe", "john.doe@labs.io", "1234567890"),
                     Customer(2, "Jane Smith", "jane.smith@labs.io", "9876543210")]
        controller = CustomerController()
        for customer in customers:
            controller.add(customer)

        assert controller.get_all() == customers

    # test the get by id method
    def test_get_by_id(self):
        customers = [Customer(1, "John Doe", "john.doe@labs.io", "1234567890"),
                     Customer(2, "Jane Smith", "jane.smith@labs.io", "9876543210")]
        controller = CustomerController()
        for customer in customers:
            controller.add(customer)

        for i in range(1, len(customers)):
            assert controller.get_by_id(i) == customers[i-1]
        assert controller.get_by_id(3) is None
