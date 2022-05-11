from flask_cors import CORS
from flask import Flask


def enable_cors(app: Flask):
    CORS(app)
