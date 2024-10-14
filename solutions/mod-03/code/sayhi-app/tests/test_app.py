import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_say_hi(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hi \xf0\x9f\x91\x8b" in response.data
