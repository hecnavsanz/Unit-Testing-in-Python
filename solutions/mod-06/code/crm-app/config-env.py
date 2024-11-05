import os


class Config:
    # at the end, these variables are not used in testing, only in development or production.
    # in tests, testcontainers create a random tcp port exposed for the container, so makes
    # no sense to use these variables in tests. use the get_connection_url() method from the
    # container object to get the connection url for the sqlalchemy engine instance in tests
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + \
                              os.environ.get('DB_USERNAME') + \
                              ':' + os.environ.get('DB_PASSWORD') + \
                              '@' + os.environ.get('DB_HOST') + \
                              ':' + os.environ.get('DB_PORT') + \
                              '/' + os.environ.get('DB_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('DATABASE_TRACK_MODIFICATIONS')
    SQLALCHEMY_ECHO = os.environ.get('DATABASE_SQL_DEBUG')
