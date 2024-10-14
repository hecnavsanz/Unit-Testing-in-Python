# -*- coding: utf-8 -*-
# test the customer model
from models.customer import Customer


class TestCustomer:

    # test the string representation
    def test_customer_string_representation(self):
        customer = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        expected_string = '{"cust_name": "John Doe", "cust_email": "john.doe@labs.io", "cust_phone": "1234567890"}'
        assert str(customer) == expected_string

    # test the string representation to recreate the customer
    def test_customer_object_string_representation(self):
        customer1 = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        customer2 = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        assert repr(customer1) == repr(customer2)

    # test the equality
    def test_customer_equality(self):
        customer1 = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        customer2 = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        assert customer1 == customer2

    # test the inequality
    def test_customer_inequality(self):
        customer1 = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        customer2 = Customer(2, "Jane Smith", "jane.smith@labs.io", "9876543210")
        assert customer1 != customer2

    # test the hash function
    def test_customer_hash(self):
        customer = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        assert hash(customer) == hash(("John Doe", "john.doe@labs.io", "1234567890"))

    # test the setters and getters
    def test_customer_setters_getters(self):
        customer = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        customer.set_name("Jane Smith")
        customer.set_email("jane.smith@labs.io")
        customer.set_phone("9876543210")
        assert customer.get_id() == 1
        assert customer.get_name() == "Jane Smith"
        assert customer.get_email() == "jane.smith@labs.io"
        assert customer.get_phone() == "9876543210"
