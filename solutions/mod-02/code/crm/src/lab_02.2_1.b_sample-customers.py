# -*- coding: utf-8 -*-
# crm app to manage customers
from controllers.customer import CustomerController
from models.customer import Customer

# create a customer controller
customer_controller = CustomerController()

# add a customer
customer = Customer(1, 'John Doe', 'john.doe@labs.io', '1234567890')
customer_controller.add(customer)
print('Customer added to list:', customer)

# add another customer
customer = Customer(2, 'Jane Smith', 'jane.smith@labs.io', '9876543210')
customer_controller.add(customer)
print('Customer added to list:', customer)

# get all the customers
print('Customers list:')
customers = customer_controller.get_all()
for customer in customers:
    print(customer)

# get the second customer by id
print('Customer in list with id 2:')
customer = customer_controller.get_by_id(2)
print(customer)

# remove the second customer
customer_controller.remove(customer)
print('Customer removed from list:', customer)

# get all the customers
print('Customers list:')
customers = customer_controller.get_all()
for customer in customers:
    print(customer)
