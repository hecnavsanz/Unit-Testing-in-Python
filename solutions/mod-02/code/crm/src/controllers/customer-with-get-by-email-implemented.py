# -*- coding: utf-8 -*-
# customer controller
from controllers.controller import Controller
from models.customer import Customer
from models.customer_exception import CustomerNotFoundException


class CustomerController(Controller):

        # constructor
        def __init__(self):
            self.customers = []

        # add a new customer
        def add(self, customer: Customer):
            self.customers.append(customer)
            return customer.get_id()

        # remove an existing customer
        def remove(self, customer: Customer):
            self.customers.remove(customer)
            return customer.get_id()

        # get all the customers
        def get_all(self):
            return self.customers

        # get a customer by id
        def get_by_id(self, id):
            for customer in self.customers:
                if customer.get_id() == id:
                    return customer
                else:
                    raise CustomerNotFoundException()

        # get a customer by email
        def get_by_email(self, email):
            for customer in self.customers:
                if customer.get_email() == email:
                    return customer
                else:
                    raise CustomerNotFoundException()
