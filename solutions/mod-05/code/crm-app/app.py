from flask import Flask
from config import Config
from flask_login import LoginManager


def create_app(config_class=Config):
    app = Flask(__name__, static_folder='views/static', template_folder='views/templates')
    app.config.from_object(config_class)

    from db.ext import db
    # sqlalchemy instance initialized with the app config object
    db.init_app(app)

    # login manager instance initialized with the app object
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models.credential import Credential

    @login_manager.user_loader
    def load_user(user_id):
        return Credential.query.get(int(user_id))

    from views.auth import auth
    from views.index import blueprint as index
    from views.customer import blueprint as customer
    app.register_blueprint(auth)
    app.register_blueprint(index)
    app.register_blueprint(customer)

    return app
