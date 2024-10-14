from flask import Blueprint, render_template, request, redirect, url_for
from db.ext import db
from models.customer import Customer


# Create the customers blueprint
blueprint = Blueprint('customers', 'customers')


# Define the route to list customers
@blueprint.route('/customer/list')
def index():
    customers = db.session.query(Customer).all()
    return render_template('customers.html', customers=customers)


# Define the route to display the form to add a customer
@blueprint.route('/customer/add', methods=['GET'])
def add():
    return render_template('customer_add.html')


# Define the route to insert a customer
@blueprint.route('/customer/add', methods=['POST'])
def insert():
    db.session.add(Customer(name=request.form['name'],
                            email=request.form['email'],
                            phone=request.form['phone'],
                            type=request.form['type']))
    db.session.commit()
    return redirect(url_for('customers.index'))


# Define the route to display the form to edit a customer
@blueprint.route('/customer/edit', methods=['GET'])
def edit():
    idn = request.args.get('id')
    customer = db.session.query(Customer).get(idn)
    return render_template('customer_edit.html', customer=customer)


# Define the route to update a customer
@blueprint.route('/customer/edit', methods=['POST'])
def update():
    idn = request.args.get('id')
    db.session.merge(Customer(id=idn,
                              name=request.form['name'],
                              email=request.form['email'],
                              phone=request.form['phone'],
                              type=request.form['type']))
    db.session.commit()
    return redirect(url_for('customers.index'))


# Define the route to delete a customer
@blueprint.route('/customer/delete', methods=['GET'])
def delete():
    idn = request.args.get('id')
    customer = db.session.get(Customer, idn)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('customers.index'))
