import pytest
from app import create_app
from db.ext import db


@pytest.fixture(scope='session')
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(scope='session')
def client(app):
    with app.test_client() as client:
        yield client
