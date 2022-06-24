from flask import Flask, Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route("/login")  # вход
def login():
    return render_template("login.html")


@auth.route("/signup")  # регистрация
def signup():
    return render_template("signup.html")


@auth.route("/logout")  # выход
def logout():
    return render_template("logout.html")
