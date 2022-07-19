from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required
from . import db

menu_manager = Blueprint('menu_manager', __name__)


@menu_manager.route('/menu_manager')
def manager():
    return render_template('menu_manager.html')