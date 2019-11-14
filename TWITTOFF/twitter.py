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