# -*- coding: utf-8 -*-
# test the customer model
from models.customer import Customer


class TestCustomer:

    # test the string representation
    def test_customer_string_representation(self):
        customer = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        expected_string = '{"cust_name": "John Doe", "cust_email": "john.doe@labs.io", "cust_phone": "1234567890"}'
        assert str(customer) == expected_string, "Customer string representation not correct"

    # test the string representation to recreate the customer
    def test_customer_object_string_representation(self):
        customer1 = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        customer2 = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        assert repr(customer1) == repr(customer2), "String representation to recreate Customer not correct"

    # test the equality
    def test_customer_equality(self):
        customer1 = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        customer2 = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        assert customer1 == customer2, "Customers are not equal"

    # test the inequality
    def test_customer_inequality(self):
        customer1 = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        customer2 = Customer(2, "Jane Smith", "jane.smith@labs.io", "9876543210")
        assert customer1 != customer2, "Customers are equal"

    # test the hash function
    def test_customer_hash(self):
        customer = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        assert hash(customer) == hash(("John Doe", "john.doe@labs.io", "1234567890")), "Customer hash not correct"

    # test the setters and getters
    def test_customer_setters_getters(self):
        customer = Customer(1, "John Doe", "john.doe@labs.io", "1234567890")
        customer.set_name("Jane Smith")
        customer.set_email("jane.smith@labs.io")
        customer.set_phone("9876543210")
        assert customer.get_id() == 1, "ID not correct"
        assert customer.get_name() == "Jane Smith", "Name not correct"
        assert customer.get_email() == "jane.smith@labs.io", "Email not correct"
        assert customer.get_phone() == "9876543210", "Phone not correct"
