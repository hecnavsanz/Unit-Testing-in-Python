# -*- coding: utf-8 -*-
# customer model class
from models.model import Model


class Product(Model):

    # constructor
    def __init__(self, id, name, category, price):
        super().__init__()
        self.id = id
        self.name = name
        self.category = category
        self.price = price

    # string representation of the product to print
    def __str__(self):
        return f"{{\"prod_id\": {str(self.id)}, \"prod_name\": \"{self.name}\", \"prod_category\": \"{self.category}\", \"prod_price\": \"{self.price}\"}}"

    # string representation to recreate the product
    def __repr__(self):
        return f'Product({self.id}, \'{self.name}\', \'{self.category}\', \'{self.price}\')'

    # compare two products are equal
    def __eq__(self, other):
        return self.name == other.name and self.category == other.category and self.price == other.price

    # compare two products are not equal
    def __ne__(self, other):
        return not self.__eq__(other)

    # hash the product
    def __hash__(self):
        return hash((self.name, self.category, self.price))

    # get the product id
    def get_id(self):
        return self.id

    # get the product name
    def get_name(self):
        return self.name

    # get the product category
    def get_category(self):
        return self.category

    # get the product price
    def get_price(self):
        return self.price

    # set the product name
    def set_name(self, name):
        self.name = name

    # set the product category
    def set_category(self, category):
        self.category = category

    # set the product price
    def set_price(self, price):
        self.price = price
