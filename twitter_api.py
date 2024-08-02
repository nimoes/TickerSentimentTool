import tweepy
import os
from dotenv import TWITTER_BEARER_TOKEN
from datetime import datetime, time, timedelta

class TwitterAPI:
    def __init__(self):
        self.client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

    def get_tweets(self, symbol, count=5):
        query = f"${symbol} -is:retweet"
        tweets = []

        # today's date
        today = datetime.now().date()

        start_time = datetime.combine(today, time.min)
        end_time = datetime.now()
