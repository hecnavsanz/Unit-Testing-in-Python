from db.ext import db
from models.customer import Customer


def test_db(app, mysql_container):
    with app.app_context():
        assert db is not None
        assert db.engine.url.database == mysql_container.dbname
        assert db.engine.url.username == mysql_container.username
        assert db.engine.url.password == mysql_container.password
        assert db.engine.url.host == 'localhost'
        assert str(db.engine.url.port) == mysql_container.get_exposed_port(3306)
        assert db.engine.url.drivername == 'mysql+pymysql'
        assert 3306 == mysql_container.port


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1 class=\'display-6\'>Welcome to the Customer Relationship Management application</h1>' in response.data


def test_customer_list_empty(app, client):
    response = client.get('/customer/list')
    assert response.status_code == 200
    assert b'<h1 class=\'display-6\'>Customers</h1>' in response.data

    with app.app_context():
        customers = db.session.query(Customer).all()
        assert len(customers) == 0


def test_customer_add(app, client):
    assert client.get('/customer/add').status_code == 200
    client.post('/customer/add', data=dict(name='Nick Fury',
                                           email='nick.fury@labs.io',
                                           phone='555-1234',
                                           type='Customer'))

    with app.app_context():
        customers = db.session.query(Customer).all()
        assert len(customers) == 1
        assert customers[0].phone == '555-1234'


def test_customer_list(app, client):
    response = client.get('/customer/list')
    assert response.status_code == 200
    assert b'<td>Nick Fury</td>' in response.data

    with app.app_context():
        customers = db.session.query(Customer).all()
        assert len(customers) == 1
        assert customers[0].name == 'Nick Fury'


def test_customer_edit(app, client):
    cust_id = None

    with app.app_context():
        customers = db.session.query(Customer).filter_by(name='Nick Fury').all()
        if len(customers) > 0:
            cust_id = customers[0].id

    client.post('/customer/edit?id=' + str(cust_id), data=dict(id=cust_id,
                                                               name='Nick Fury',
                                                               email='nick.fury@labs.io',
                                                               phone='(123) 555-1234',
                                                               type='Customer'))

    with app.app_context():
        customers = db.session.query(Customer).all()
        assert len(customers) == 1
        assert customers[0].phone == '(123) 555-1234'


def test_customer_delete(app, client):
    cust_id = None

    with app.app_context():
        customers = db.session.query(Customer).filter_by(name='Nick Fury').all()
        if len(customers) > 0:
            cust_id = customers[0].id

    client.get('/customer/delete?id=' + str(cust_id))

    with app.app_context():
        customers = db.session.query(Customer).all()
        assert len(customers) == 0
