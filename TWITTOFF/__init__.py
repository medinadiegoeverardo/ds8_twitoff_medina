""" Entry point for twitoff app """

from .app import create_app

# global
APP = create_app()

# run with: FLASK_APP=TWITTOFF:APP flask run
