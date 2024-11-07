import pytest
import sqlalchemy
from app import create_app
from config import Config
from db.ext import db
from testcontainers.mysql import MySqlContainer


@pytest.fixture(scope='session')
def load_env_vars():
    import os
    db_vars = {'DB_USERNAME': os.environ.get('DB_USERNAME'),
               'DB_PASSWORD': os.environ.get('DB_PASSWORD'),
               'DB_HOST': os.environ.get('DB_HOST'),
               'DB_PORT': os.environ.get('DB_PORT'),
               'DB_NAME': os.environ.get('DB_NAME')}
    return db_vars


# The database fixture is responsible for creating a MySQL container
# and returning the connection URL.
@pytest.fixture(scope='session')
def mysql_container(load_env_vars):
    with MySqlContainer('mysql:8.0',
                        load_env_vars["DB_USERNAME"],
                        load_env_vars["DB_PASSWORD"],
                        load_env_vars["DB_PASSWORD"],
                        load_env_vars["DB_NAME"],
                        int(load_env_vars["DB_PORT"]),
                        'tests/data') as mysql:
        conn_url = mysql.get_connection_url()
        # this is just to show the connection id, the container is already running
        engine = sqlalchemy.create_engine(conn_url)
        with engine.begin() as connection:
            print(mysql.get_connection_url())
            connection_id = connection.execute(sqlalchemy.text('select connection_id()'))
            print('Connection ID: ' + str(connection_id.fetchone()))

        # wait here to run tests and when done come back to clean up the container
        yield mysql


# The app fixture is responsible for creating the Flask application
# If the database fixture is not None, the Config object is created with the TestContainers
# database URL, and it will use the TestContainers MySQL container during testing.
@pytest.fixture(scope='session')
def app(mysql_container):
    # if the TestContainers MySQL container is running, use it, if not use the manual MySQL container
    if mysql_container is not None:
        config = Config(mysql_container.get_connection_url(), False, True)
    else:
        config = Config()
    app = create_app(config)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


# The client fixture is responsible for creating a test client for the Flask application.
@pytest.fixture(scope='session')
def client(app):
    app.testing = True  # to propagate the exceptions to the test client
    with app.test_client() as client:
        yield client
