""" Minimal Flask app"""

from flask import Flask

# make application
app = Flask(__name__)

# decorator: this tells you where to go (router)
@app.route("/") # /username

# define function
def hello():
    return 'hello'