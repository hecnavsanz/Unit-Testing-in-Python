# -*- coding: utf-8 -*-
# test the customer controller
from controllers.customer import CustomerController
from models.customer_exception import CustomerNotFoundException
import pytest


class TestCustomerController:

    # test the add method
    @pytest.mark.modify
    def test_add(self, a_customer):
        controller = CustomerController()
        customer = a_customer
        idn = a_customer.get_id()

        assert controller.add(customer) == idn, "Customer not added"

    # test the remove method
    @pytest.mark.modify
    def test_remove(self, another_customer):
        controller = CustomerController()
        customer = another_customer
        idn = another_customer.get_id()
        controller.add(customer)

        assert controller.remove(customer) == idn, "Customer not removed"

    # test the get all method
    @pytest.mark.query
    def test_get_all(self, some_customers, a_customer, another_customer):
        controller = CustomerController()
        controller.add(a_customer)
        controller.add(another_customer)

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
    def test_get_by_email(self, another_customer):
        controller = CustomerController()
        customer = another_customer
        email = another_customer.get_email()
        controller.add(customer)

        assert controller.get_by_email(email) == customer, "Customer not found"

        with pytest.raises(CustomerNotFoundException) as e:
            controller.get_by_email("joe.fresh@labs.io") == customer
        assert "Customer not found" in str(e.value), "No CustomerNotFoundException raised"
