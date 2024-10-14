# -*- coding: utf-8 -*-
# abstract controller class
from abc import ABC, abstractmethod


class Controller(ABC):

    # abstract controller class
    def __init__(self):
        pass

    # add a new object
    @abstractmethod
    def add(self, obj):
        pass

    # remove an existing object
    @abstractmethod
    def remove(self, obj):
        pass

    # get all the objects
    @abstractmethod
    def get_all(self):
        pass

    # get an object by id
    @abstractmethod
    def get_by_id(self, idn):
        pass
