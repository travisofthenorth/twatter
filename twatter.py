import os
import sys
import tweepy
from stream import TwatStreamListener
from multiprocessing import Process

auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_SECRET'])

search_terms = sys.argv[1:]
stream_listener = TwatStreamListener(search_terms)

twat_stream = tweepy.Stream(auth = auth, listener=stream_listener)
twat_stream.filter(track=search_terms)
