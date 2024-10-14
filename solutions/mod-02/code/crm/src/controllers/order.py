# -*- coding: utf-8 -*-
# order controller
from controllers.controller import Controller
from models.order_exception import OrderNotFoundException


class OrderController(Controller):

    # constructor
    def __init__(self):
        self.orders = []

    # add a new order
    def add(self, order):
        self.orders.append(order)
        return order.get_id()

    # remove an existing order
    def remove(self, order):
        self.orders.remove(order)
        return order.get_id()

    # get all the orders
    def get_all(self):
        return self.orders

    # get an order by id
    def get_by_id(self, id):
        for order in self.orders:
            if order.get_id() == id:
                return order
            else:
                raise OrderNotFoundException()

    # get orders by customer
    def get_by_customer(self, customer):
        orders = []
        for order in self.orders:
            if order.getCustomer() == customer:
                orders.append(order)
        return orders

    # get orders by product
    def get_by_product(self, product):
        orders = []
        for order in self.orders:
            if order.getProduct() == product:
                orders.append(order)
        return orders
