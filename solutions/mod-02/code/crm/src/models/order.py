# -*- coding: utf-8 -*-
# order model class
import json
from models.model import Model


class Order(Model):

    # constructor
    def __init__(self, idn, customer, product, quantity):
        super().__init__()
        self.idn = idn
        self.customer = customer
        self.product = product
        self.quantity = quantity

    # string representation of the order to print
    def __str__(self):
        return json.dumps({'ord_id': str(self.idn), 'ord_customer': self.customer, 'ord_product': self.product,
                           'ord_quantity': self.quantity})

    # string representation to recreate the order
    def __repr__(self):
        return f'Order({self.idn}, {self.customer}, {self.product}, {self.quantity})'

    # compare two orders are equal
    def __eq__(self, other):
        return (self.customer, self.product, self.quantity) == (other.customer, other.product, other.quantity)

    # compare two orders are not equal
    def __ne__(self, other):
        return not self.__eq__(other)

    # hash the order
    def __hash__(self):
        return hash((self.customer, self.product, self.quantity))

    # get the order id
    def get_id(self):
        return self.idn

    # get the customer
    def getCustomer(self):
        return self.customer

    # get the product
    def getProduct(self):
        return self.product

    # get the quantity
    def getQuantity(self):
        return self.quantity

    # set the customer
    def setCustomer(self, customer):
        self.customer = customer

    # set the product
    def setProduct(self, product):
        self.product = product

    # set the quantity
    def setQuantity(self, quantity):
        self.quantity = quantity
