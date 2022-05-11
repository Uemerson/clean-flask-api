from flask import Flask
from src.main.config.middlewares import setup_middlewares


def create_app():
    app = Flask(__name__)
    setup_middlewares(app)
    return app
