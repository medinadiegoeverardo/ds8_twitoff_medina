""" Retrieving tweets, embeddings, and save into database """

import basilica
import tweepy
from decouple import config
from .model import DB, Tweet, User

# connecting to API
# documentation from Tweepy (to do it this way)
TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'), config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(config('BASILICA_KEY'))

# accessing twitter!
# def add_or_update_user():
#     """ Add or update user and their tweets, else error """
#     try: # add user
#         twitter_user = TWITTER.get_user(username)
#         db_user = (User.query.get(twitter_user.id) or # adding or updating
#         User(id=twitter_user.id, name=username))

#         DATABASE.session.add(db_user)
#         tweets = twitter_user.timeline(count=200, exlude_replies=True,
#         include_rts=False, tweet_mode='extended', since_id=db_user.newest_tweet_id)

#         if tweets:
#              db_user.newest_tweet_id = tweet[0].id
#         for tweet in tweets:
#             embedding = BASILICA.embed_sentence(tweet.full_text, model='twitter')
#             db_tweet = Tweet(tweet)

#     except Exception as e:
#         pass
