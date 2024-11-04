import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'mysql+pymysql://labs:Pytest-TDD.Labs_4ALL@localhost:3306/crmdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.environ.get('DATABASE_SQL_DEBUG') or True
