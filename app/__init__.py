from flask import Flask
from flask_httpauth import HTTPTokenAuth
from app.config import config
import os

auth = HTTPTokenAuth(scheme='Bearer')
tokens = os.environ.get('TOKENS').split()


def create_app():
    # Create application
    app = Flask(__name__)
    app.config.from_object(config)

    from app.base import base as views_blueprint
    app.register_blueprint(views_blueprint)


    # Create admin

    return app
