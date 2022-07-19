from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# pip install flask
# pip install Flask-Login
# pip install Flask-SQLAlchemy
# npm install bulma

# set FLASK_APP=sookla_project
# set FLASK_DEBUG=1
# flask run

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'feagrhgadsjgxbncvbdrharhanafdhadfhafhert3434t43DGSDFGDAFG'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .signup import signup as signup_blueprint
    app.register_blueprint(signup_blueprint)

    from .menu_manager import menu_manager as menu_manager_blueprint
    app.register_blueprint(menu_manager_blueprint)

    from .display_menu import display_menu as display_menu_blueprint
    app.register_blueprint(display_menu_blueprint)

    return app
