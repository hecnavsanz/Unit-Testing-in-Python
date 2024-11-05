import pytest
from db.ext import db
from models.customer import Customer
from sqlalchemy import select

@pytest.fixture(autouse=True)
def setup_tables(app):
    with app.app_context():
        db.create_all()
        yield
        db.drop_all()

@pytest.fixture
def customer():
    return Customer(name='John Doe',
                    email='john.doe@labs.io',
                    phone='(123) 456-7890',
                    type='Customer')

def test_customer_creation(customer, app):
    with app.app_context():
        db.session.add(customer)
        db.session.commit()

        customer_id = customer.id
        expected_customer = db.session.execute(
            select(Customer).filter_by(id=customer_id)
            ).scalar_one()

        assert customer.id == expected_customer.id and \
               customer.name == expected_customer.name and \
               customer.email == expected_customer.email and \
               customer.phone == expected_customer.phone and \
               customer.type == expected_customer.type
