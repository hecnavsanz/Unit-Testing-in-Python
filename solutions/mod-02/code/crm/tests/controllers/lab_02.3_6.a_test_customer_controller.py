# -*- coding: utf-8 -*-
# test the customer controller
from controllers.customer import CustomerController
from models.customer import Customer
from models.customer_exception import CustomerNotFoundException
import pytest
import sys


@pytest.mark.parametrize("idn, name, email, phone", [(1, "John Doe", "john.doe@labs.io", "1234567890"),
                                                     (2, "Jane Smith", "jane.smith@labs.io", "9876543210"),
                                                     pytest.param(3, "James King", "james.king@labs.io",
                                                                  "1234554321", marks=[pytest.mark.not_a_customer])])
# other way to parametrize the test using pytestmark instead of the decorator
# pytestmark = pytest.mark.parametrize("id, name, email, phone",[(1, "John Doe", "john.doe@labs.io", "1234567890"),
#                                                                (2, "Jane Smith", "jane.smith@labs.io", "9876543210")])
class TestCustomerController:

    # test the add method
    @pytest.mark.modify
    def test_add(self, idn, name, email, phone):
        controller = CustomerController()
        customer = Customer(idn, name, email, phone)

        assert controller.add(customer) == idn, "Customer not added"

    # test the remove method
    @pytest.mark.modify
    def test_remove(self, idn, name, email, phone):
        controller = CustomerController()
        customer = Customer(idn, name, email, phone)
        controller.add(customer)

        assert controller.remove(customer) == idn, "Customer not removed"

    # test the get all method
    @pytest.mark.query
    @pytest.mark.skip(reason="CustomerController.get_all method not tested")
    def test_get_all(self, idn, name, email, phone):
        controller = CustomerController()
        customer = Customer(idn, name, email, phone)
        controller.add(customer)

        assert controller.get_all() == [customer], "Customers not found"

    # test the get by id method
    @pytest.mark.query
    def test_get_by_id(self, idn, name, email, phone):

        if sys.version_info >= (3, 11):
            pytest.skip("Requires Python 3.11 or higher")

        controller = CustomerController()
        customer = Customer(idn, name, email, phone)
        controller.add(customer)

        assert controller.get_by_id(idn) == customer, "Customer not found"

        with pytest.raises(CustomerNotFoundException) as e:
            controller.get_by_id(3) == customer
        assert "Customer not found" in str(e.value), "No CustomerNotFoundException raised"

    # test the get by email method
    @pytest.mark.query
    @pytest.mark.xfail(reason="CustomerController.get_by_email method not implemented", run=True)
    def test_get_by_email(self, idn, name, email, phone):
        controller = CustomerController()
        customer = Customer(idn, name, email, phone)
        controller.add(customer)

        assert controller.get_by_email(email) == customer, "Customer not found"
