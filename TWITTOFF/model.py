""" Create database model/tables """

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# structure for database that store info from (or in?) Twitter

# created using DB.create_all()
# ^ should give me empty db.sqlite3
# after this: add data into database (DB.session.add(x))

class User(DB.Model):
    """ Twitter users that we analyze, creating table """

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False) # cannot be null


class Tweet(DB.Model):
    """ Users' tweets from Twitter """
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))
