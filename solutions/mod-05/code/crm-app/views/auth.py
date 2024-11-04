from flask import request, flash, redirect, url_for
from models.credential import Credential
from flask import Blueprint, render_template
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    username = request.form.get('username')
    password = request.form.get('password')

    cred = Credential.query.filter_by(username=username).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not cred or not cred.password == password:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(username, remember=True)
    return redirect(url_for('index.index'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))
