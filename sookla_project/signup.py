from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required
from . import db

signup = Blueprint('signup', __name__)


@signup.route('/registration')
def register():
    return render_template('register.html')


@signup.route('/registration', methods=['POST'])
def register_post():
    try:

        name = request.form.get('name')
        password = request.form.get('password')
        admin_pass = request.form.get('admin_pass')

        user = User.query.filter_by(
            name=name).first()  # if this returns a user, then the email already exists in database

        if user or admin_pass != "1010":  # if a user is found, we want to redirect back to signup page so user can try again
            flash('Ошибка!')
            return redirect(url_for('signup.register'))
    except Exception as e:
        db.session.rollback()
        print(e)

    new_user = User(name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    # db.session.flush()
    db.session.commit()
    flash('Пользователь создан')

    return redirect(url_for('auth.login'))
