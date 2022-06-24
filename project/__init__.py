# pip install flask
# pip install Flask-Login
# pip install Flask-SQLAlchemy
# npm install bulma

# set FLASK_APP=project
# set FLASK_DEBUG=1
# flask run

from flask import Flask
from  flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'JGUKGJBMKBJKGJKBjhjkhjkhjkhk;lhjh'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

