from behave import fixture, use_fixture
import sqlalchemy
from app import create_app
from config import Config
from db.ext import db
from testcontainers.mysql import MySqlContainer


# The database fixture is responsible for creating a MySQL container
# and returning the connection URL.
@fixture
def mysql_container(context):
    with MySqlContainer('mysql:8.0',
                        "labs",
                        "Pytest-TDD.Labs_4ALL",
                        "Pytest-TDD.Labs_4ALL",
                        "crmdb",
                        3306,
                        'tests/data') as mysql:

        # wait here to run tests and when done come back to clean up the container
        context.mysql = mysql
        yield context.mysql


# The app fixture is responsible for creating the Flask application
# If the database fixture is not None, the Config object is created with the TestContainers
# database URL, and it will use the TestContainers MySQL container during testing.
@fixture
def app(context):
    config = Config(context.mysql.get_connection_url())
    app = create_app(config)
    app.testing = True
    context.app = app
    with context.app.app_context():
        db.create_all()
        yield context.app


# The client fixture is responsible for creating a test client for the Flask application.
@fixture
def client(context):
    with context.app.test_client() as client:
        context.client = client
        yield context.client


# when there are multiple features, use the before_all hook)
def before_all(context):
    use_fixture(mysql_container, context)
    use_fixture(app, context)


# there's only one feature in this project but recreate the client for each feature
def before_scenario(context, scenario):
    use_fixture(client, context)
