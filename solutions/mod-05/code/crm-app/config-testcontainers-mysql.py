import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') \
                              or 'mysql+pymysql://labs:Pytest-TDD.Labs_4ALL@localhost:3306/crmdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.environ.get('DATABASE_SQL_DEBUG') or True

    # The overloaded constructor is using parameters to override default settings.
    def __init__(self, sa_db_uri, sa_track_notif, sa_echo):
        self.SQLALCHEMY_DATABASE_URI = sa_db_uri
        self.SQLALCHEMY_TRACK_MODIFICATIONS = sa_track_notif
        self.SQLALCHEMY_ECHO = sa_echo
