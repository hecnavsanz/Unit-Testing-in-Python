# -*- coding: utf-8 -*-
# customer exceptions

# customer not found exception
class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer not found"):
        self.message = message
        super().__init__(self.message)
