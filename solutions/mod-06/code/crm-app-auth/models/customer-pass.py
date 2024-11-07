# -*- coding: utf-8 -*-
# customer model
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Enum
from db.ext import db
from typing import Literal


class Customer(db.Model):

    __tablename__ = 'customers'

    customer_types = Literal['Employee',
                             'Customer',
                             'Vendor',
                             'Partner']

    customer_enum = Enum('Employee','Customer','Vendor','Partner',
                         name="cust_type_enum")

    id: Mapped[int] = mapped_column('cust_id', Integer,
                                    primary_key=True, unique=True,
                                    nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column('cust_name', String(120),
                                      nullable=False)
    email: Mapped[str] = mapped_column('cust_email', String(160),
                                       nullable=False)
    phone: Mapped[str] = mapped_column('cust_phone', String(14),
                                       nullable=False)
    type: Mapped[customer_types] = mapped_column(customer_enum,
                                                 nullable=False,
                                                 name='cust_type')

