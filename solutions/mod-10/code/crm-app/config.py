import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'mysql+pymysql://labs:Pytest-TDD.Labs_4ALL@34.55.206.111:13306/crmdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.environ.get('DATABASE_SQL_DEBUG') or True

    SECRET_KEY = 'th3-s3cr3t-1s-n0t-s3cr3t'
