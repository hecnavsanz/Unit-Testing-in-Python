# -*- coding: utf-8 -*-
# customer controller using file storage
from controllers.controller import Controller
from models.customer import Customer
from models.customer_exception import CustomerNotFoundException
from utils.file_storage import FileStorage
import json


class CustomerController(Controller):

    # constructor
    def __init__(self, storage: FileStorage, logger=None):
        # self.customers = []
        super().__init__()
        self.storage = storage
        if logger:
            self.__logger = logger
        self.__logger.info("Database initialized")

    # add a new customer method
    def add(self, customer: Customer):
        self.storage.write(customer)
        self.__logger.info("Customer added")
        return str(customer)

    # remove an existing customer method
    def remove(self, customer: Customer):
        self.storage.remove(customer)
        self.__logger.info("Customer removed")
        return str(customer)

    # change an existing customer method
    def change(self, old_customer: Customer, new_customer: Customer):
        self.storage.modify(old_customer, new_customer)
        self.__logger.info("Customer modified")
        return str(new_customer)

    # get all the customers method
    def get_all(self):
        self.__logger.info("Getting all customers")
        return self.storage.read_all()

    # get a customer by key private method
    def __get_by_key(self, key, value):
        for customer in self.storage.read_all():
            cust_json = json.loads(customer)
            if cust_json[key] == value:
                self.__logger.info("Customer found")
                return str(Customer(cust_json['cust_id'],
                                    cust_json['cust_name'],
                                    cust_json['cust_email'],
                                    cust_json['cust_phone']))

        self.__logger.error("Customer not found")
        raise CustomerNotFoundException()

    # get a customer by id method
    def get_by_id(self, idn):
        self.__logger.info("Getting customer by id (" + str(idn) + ")")
        return self.__get_by_key("cust_id", idn)

    # get a customer by email method
    def get_by_email(self, email):
        self.__logger.info("Getting customer by email (" + email + ")")
        return self.__get_by_key("cust_email", email)
