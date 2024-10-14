import pytest
from app import create_app
from db.ext import db


@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


def test_db(app):
    with app.app_context():
        assert db is not None
        assert db.engine.url.database == 'crmdb'
        assert db.engine.url.username == 'labs'
        assert db.engine.url.password == 'Pytest-TDD.Labs_4ALL'
        assert db.engine.url.host == 'localhost'
        assert db.engine.url.port == 3306


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>CRM Application</h1>' in response.data
