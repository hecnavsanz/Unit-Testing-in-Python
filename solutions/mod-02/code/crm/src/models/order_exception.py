# -*- coding: utf-8 -*-
# order exceptions


# order not found exception
class OrderNotFoundException(Exception):
    def __init__(self, message="Order not found"):
        self.message = message
        super().__init__(self.message)
