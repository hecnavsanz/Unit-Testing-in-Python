# -*- coding: utf-8 -*-
# customer controller
from controllers.controller import Controller
from models.product import Product
from models.product_exception import ProductNotFoundException


class ProductController(Controller):

    # constructor
    def __init__(self):
        self.products = []

    # add a new product
    def add(self, product: Product):
        self.products.append(product)
        return product.get_id()

    # remove an existing product
    def remove(self, product: Product):
        self.products.remove(product)
        return product.get_id()

    # get all the products
    def get_all(self):
        return self.products

    # get a product by id
    def get_by_id(self, id):
        for product in self.products:
            if product.get_id() == id:
                return product
            else:
                raise ProductNotFoundException()

    # get a product by name
    def get_by_name(self, name):
        for product in self.products:
            if product.get_name() == name:
                return product
        return None

    # get products by category
    def get_by_category(self, category):
        products = []
        for product in self.products:
            if product.get_category() == category:
                products.append(product)
        return products
