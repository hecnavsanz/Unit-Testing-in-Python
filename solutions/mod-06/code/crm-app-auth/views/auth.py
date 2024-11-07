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
    remember = True if request.form.get('remember') else False

    cred = Credential.query.filter_by(username=username).first()

    if cred is None or not cred.username == username or not cred.password == password:
        flash('Please check your login credentials and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    login_user(cred, remember=remember)
    return redirect(url_for('index.index'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))
