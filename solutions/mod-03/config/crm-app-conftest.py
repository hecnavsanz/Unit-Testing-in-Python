import pytest
from app import create_app


@pytest.fixture(scope='session')
def app():
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture(scope='session')
def client(app):
    with app.test_client() as client:
        yield client
