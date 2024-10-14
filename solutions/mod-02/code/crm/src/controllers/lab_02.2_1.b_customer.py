# -*- coding: utf-8 -*-
# customer controller
from controllers.controller import Controller
from models.customer import Customer


class CustomerController(Controller):

    # constructor
    def __init__(self):
        super().__init__()
        self.customers = []

    # add a new customer
    def add(self, customer: Customer):
        self.customers.append(customer)
        return customer.get_id()

    # remove an existing customer
    def remove(self, customer: Customer):
        cust_idx = self.customers.index(customer)
        self.customers.pop(cust_idx)
        return customer.get_id()

    # get all the customers
    def get_all(self):
        return self.customers

    # get a customer by id
    def get_by_id(self, idn):
        for customer in self.customers:
            if customer.get_id() == idn:
                return customer
        return None
