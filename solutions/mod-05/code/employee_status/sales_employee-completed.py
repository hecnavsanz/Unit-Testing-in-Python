# File: sales_employee.py
from datetime import time


class SalesEmployee:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.type = 'sales'

    def get_type(self):
        return self.type

    @staticmethod
    def is_online(date_time):
        if (date_time.weekday() in range(5, 6)) or \
            (date_time.weekday() in range(0, 4) and
             (date_time.time() < time(9, 0) or
              date_time.time() > time(18, 0))):
            return False
        else:
            return True
