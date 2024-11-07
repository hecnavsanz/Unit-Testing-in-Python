# -*- coding: utf-8 -*-
# credential model
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String
from flask_login import UserMixin
from db.ext import db


class Credential(UserMixin, db.Model):
    __tablename__ = 'credentials'

    id: Mapped[int] = mapped_column('cred_id', Integer,
                                    primary_key=True, unique=True,
                                    nullable=False, autoincrement=True)
    username: Mapped[str] = mapped_column('cred_username', String(120),
                                          nullable=False)
    password: Mapped[str] = mapped_column('cred_password', String(160),
                                          nullable=False)
