""" Create database model/tables """

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# structure for database that store info from (or in?) Twitter

# created using DB.create_all()
# ^ should give me empty db.sqlite3
# after this: add data into database (DB.session.add(x))

class User(DB.Model):
    """ Twitter users that we analyze, creating table """

    id = DB.Column(DB.BigInteger, primary_key=True) # delete database to replace Integer to BigInteger
    name = DB.Column(DB.String(15), nullable=False) # cannot be null (required)
    newest_tweet_id = DB.Column(DB.BigInteger) # not necessary but to keep track of newest tweet

    # formatting
    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweet(DB.Model):
    """ Users' tweets from Twitter """
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False) # cannot be null (required)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True)) # back reference it. relationship to user
    # user_id and user are to have that one to many relationship between users and tweets
    
    # storing embedding in database - pickle is standard for serializing
    embedding = DB.Column(DB.PickleType, nullable=False) # PickleType is a new type

    # formatting
    def __repr__(self):
        return '<Tweet {}>'.format(self.text)