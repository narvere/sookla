from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# pip install flask
# pip install Flask-Login
# pip install Flask-SQLAlchemy
# npm install bulma

# set FLASK_APP=bulma2
# set FLASK_DEBUG=1
# flask run

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["PUBLIC_KEY"] = "HJFHJGLHGHkj564524654j"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
