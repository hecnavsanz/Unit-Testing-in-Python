import pytest
from app import create_app

# The app fixture creates an instance of the Flask application
@pytest.fixture(scope='session')
def app():
    app = create_app()
    yield app

# The app_ctx fixture creates a context for the Flask application
@pytest.fixture(scope='session')
def app_ctx(app):
    with app.app_context() as ctx:
        yield ctx

# The client fixture creates a test client for the Flask application
@pytest.fixture(scope='session')
def client(app):
    with app.test_client() as client:
        yield client
