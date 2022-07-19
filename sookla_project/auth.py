from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required
from . import db

auth = Blueprint('auth', __name__)



@auth.route('/')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    try:
        name = request.form.get('name')
        password = request.form.get('password')
        # remember = True if request.form.get('remember') else False

        user = User.query.filter_by(name=name).first()
    except Exception as e:
        print(e)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user)
    return redirect(url_for('menu_manager.manager'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    print('Вышли')
    return redirect(url_for('auth.login'))