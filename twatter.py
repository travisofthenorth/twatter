import os
import tweepy
from stream import TwatStreamListener
from multiprocessing import Process

auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_SECRET'])

def stream_twats(search):
    stream_listener = TwatStreamListener(search)
    twat_stream = tweepy.Stream(auth = auth, listener=stream_listener)
    twat_stream.filter(track=[search])

if __name__ == '__main__':
    for search in ('cat', 'dog'):
        p = Process(target=stream_twats, args=(search,))
        p.start()
