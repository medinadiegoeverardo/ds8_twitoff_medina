""" database models """

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# # databases that store info from (or in?) Twitter
# # 2 tables

class User(DB.Model):
    """ Twitter users that we analyze, creating table """

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False) # cannot be null


class Tweet(DB.Model):
    """ Users' tweets from Twitter """
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))
