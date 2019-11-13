""" Minimal Flask app"""

from flask import Flask, render_template

# make application
app = Flask(__name__)

# decorator: this tells you where to go (router)
@app.route("/") # /username

# define function
def hello():
    return render_template("home.html")

# another route
@app.route("/about")

# another function
def another():
    return render_template("page.html")