import os
import sys
import tweepy
from stream import TwitStreamListener

auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_SECRET'])

search_terms = sys.argv[1:]
stream_listener = TwitStreamListener(search_terms)

twit_stream = tweepy.Stream(auth = auth, listener=stream_listener)
twit_stream.filter(track=search_terms)
