from flask import Flask

from .bug import bug_blueprint
from .routes import main_routes


def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile("config.py")
    app.register_blueprint(main_routes)
    app.register_blueprint(bug_blueprint, url_prefix="/bug")
    return app
