import tweepy
import os
from config import TWITTER_BEARER_TOKEN
from datetime import datetime, time, timedelta

class TwitterAPI:
    def __init__(self):
        self.client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

    def get_tweets(self, symbol, count=10):
        # prepend symbol with '$' if it's not included
        if not symbol.startswith("$"):
            symbol = f"\${symbol}"
        query = f"\${symbol} -is:retweet lang:en"
        tweets = []

        # today's date
        today = datetime.now().date()

        start_time = datetime.combine(today, time.min)
        end_time = datetime.now()

        try:
            for tweet in tweepy.Paginator(self.client.search_recent_tweets, query=query, tweet_fields=['created_at', 'public_metrics'], max_results=10).flatten(limit=count):
                tweets.append({
                    'text': tweet.text,
                    'created_at': tweet.created_at,
                    'user': tweet.author_id,
                    'retweet_count': tweet.public_metrics['retweet_count'],
                    'favorite_count': tweet.public_metrics['like_count']
                    })
            print(tweets)
            return tweets
        # base exception for Tweepy
        except tweepy.errors.TweepyException as e:
            print(f"Error: {e}")
            return []

# test
if __name__ == "__main__":
    from config import TWITTER_BEARER_TOKEN
    twitter_api = TwitterAPI()

    # test with known symbols
    test_symbol = "GOOGL"
    tweet_count = 10

    print(f"Fetching last {tweet_count} tweets on ${test_symbol}")

    tweets = twitter_api.get_tweets(test_symbol, count=tweet_count)

    if tweets:
        print(f"Here is the last {len(tweets)} on {test_symbol}..")
        print(tweets)
        print(dir(tweets))
    else:
        print(f"No tweets pertainiing to {test_symbol}")
