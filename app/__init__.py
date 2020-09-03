from flask import Flask
from flask_httpauth import HTTPTokenAuth
from app.config import config
import os, sys
import logging

auth = HTTPTokenAuth(scheme='Bearer')
tokens = os.environ.get('TOKENS').split()
log = logging.getLogger()

def create_app():
    # Create application
    app = Flask(__name__)
    app.config.from_object(config)

    # Logging
    out_hdlr = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    out_hdlr.setFormatter(fmt)
    out_hdlr.setLevel(logging.INFO)
    # append to the global logger.
    log.addHandler(out_hdlr)
    log.setLevel(logging.INFO)

    from app.base import base as views_blueprint
    app.register_blueprint(views_blueprint)


    # Create admin

    return app
