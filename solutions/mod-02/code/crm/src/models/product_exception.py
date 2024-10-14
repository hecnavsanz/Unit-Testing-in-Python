# -*- coding: utf-8 -*-
# product exceptions


# product not found exception
class ProductNotFoundException(Exception):
    def __init__(self, message="Product not found"):
        self.message = message
        super().__init__(self.message)
