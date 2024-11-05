from db.ext import db


def test_db(app):
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
