# -*- coding: utf-8 -*-
# customer model class
import json
from models.model import Model


class Customer(Model):

    # constructor
    def __init__(self, idn, name, email, phone):
        super().__init__()
        self.__idn = idn
        self.__name = name
        self.__email = email
        self.__phone = phone

    # json representation of the customer to print
    def __str__(self):
        return json.dumps({'cust_id': self.__idn, 'cust_name': self.__name, 'cust_email': self.__email,
                           'cust_phone': self.__phone})

    # string representation to recreate the customer
    def __repr__(self):
        return f'Customer({self.__idn}, \'{self.__name}\', \'{self.__email}\', \'{self.__phone}\')'

    # compare two customers are equal
    def __eq__(self, other):
        return (self.__name, self.__email, self.__phone) == (other.get_name(), other.get_email(), other.get_phone())

    # compare two customers are not equal
    def __ne__(self, other):
        return not self.__eq__(other)

    # hash the customer
    def __hash__(self):
        return hash((self.__name, self.__email, self.__phone))

    # get the customer id
    def get_id(self):
        return self.__idn

    # get the customer name
    def get_name(self):
        return self.__name

    # get the customer email
    def get_email(self):
        return self.__email

    # get the customer phone number
    def get_phone(self):
        return self.__phone

    # set the customer name
    def set_name(self, name):
        self.__name = name

    # set the customer email
    def set_email(self, email):
        self.__email = email

    # set the customer phone number
    def set_phone(self, phone):
        self.__phone = phone
