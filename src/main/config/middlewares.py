from flask import Flask
from src.main.middlewares.cors import enable_cors


def setup_middlewares(app: Flask):
    enable_cors(app)
