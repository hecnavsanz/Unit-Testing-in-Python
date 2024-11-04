from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__, static_folder='views/static', template_folder='views/templates')
    app.config.from_object(config_class)

    from db.ext import db
    # sqlalchemy instance initialized with the app config object
    db.init_app(app)

    from views.index import blueprint as index
    from views.customer import blueprint as customer
    app.register_blueprint(index)
    app.register_blueprint(customer)

    return app
