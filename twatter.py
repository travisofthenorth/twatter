import os
import redis
import tweepy
from tweepy.utils import import_simplejson

class TwatStreamListener(tweepy.StreamListener):

    json_parser = import_simplejson()
    twat_redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    def on_connect(self):
        print('connected!')

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)

    def on_data(self, raw_data):
        data = self.json_parser.loads(raw_data)
        self.traverse(data)

    def traverse(self, twat):
        for attribute, value in twat.iteritems():
            if isinstance(value, dict):
                self.traverse(value)
            if isinstance(value, list):
                self.collect_images(value)

    def collect_images(self, l):
        image_list = []
        for obj in l:
            if type(obj) is not dict:
                continue
            img_url = obj.get('media_url_https', None)
            if img_url is not None:
                image_list.append(img_url)

        if len(image_list) > 0:
            self.push_image_list(list(set(image_list)))

    def push_image_list(self, urls):
        self.twat_redis.lpush('twats', *urls)


auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_SECRET'])

stream_listener = TwatStreamListener()
twat_stream = tweepy.Stream(auth = auth, listener=stream_listener)

twat_stream.filter(track=['trump'])
