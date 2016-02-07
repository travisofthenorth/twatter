import os
import tweepy
from stream import TwatStreamListener

auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_SECRET'])

stream_listener = TwatStreamListener('trump')
twat_stream = tweepy.Stream(auth = auth, listener=stream_listener)

twat_stream.filter(track=['trump'])
