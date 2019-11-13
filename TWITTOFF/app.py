""" Function for __init__ """

from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")

    def root():
        return 'Testing, testing'
    return app