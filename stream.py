import os
import redis
import time
import datetime
import tweepy
from tweepy.utils import import_simplejson
# from data import Postgres

class TwatStreamListener(tweepy.StreamListener):

    json_parser = import_simplejson()
    twat_redis = redis.StrictRedis(
        host=os.environ['REDIS_HOST'],
        port=os.environ['REDIS_PORT'],
        password=os.environ['REDIS_PASSWORD']
    )

    def __init__(self, search_terms):
        super(TwatStreamListener, self).__init__()
        self.search_terms = search_terms

    def on_connect(self):
        print('connected!')

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)

    def on_data(self, raw_data):
        data = self.json_parser.loads(raw_data)
        if data.has_key('id'):
            self.traverse(data['id'], data)

    def match(self, twat, phrase):
        for word in phrase.split(' '):
            if word in twat:
                return True
        return False

    def record(self, twat, phrase):
        time = self.to_datetime(twat.get('timestamp_ms', None))
        Postgres().insert_twat(search = phrase, text = twat['text'],
            location = twat['user']['location'], tweeted_at = time)

    def to_datetime(self, timestamp):
        if timestamp is None:
            timestamp = time.time() * 1000
        time = int(timestamp) / 1000
        return datetime.datetime.fromtimestamp(time)

    def traverse(self, id, twat):
        for attribute, value in twat.iteritems():
            if isinstance(value, dict):
                self.traverse(id, value)
            if isinstance(value, list):
                self.collect_images(id, value)

    def collect_images(self, id, l):
        for obj in l:
            if type(obj) is not dict:
                continue
            img_url = obj.get('media_url_https', None)
            if img_url is not None:
                self.push_image(id, img_url)


    def push_image(self, id, url):
        twat_link = 'https://twitter.com/statuses/%s' % id
        data = { 'image': url, 'status': twat_link}
        self.twat_redis.hmset('twatter_image', data)

    def push_image_list(self, urls):
        if type(urls) == list and len(urls) > 0:
            self.twat_redis.lpush('twats', *urls)
