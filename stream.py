import redis
import datetime
import tweepy
from tweepy.utils import import_simplejson
from data import Postgres

class TwatStreamListener(tweepy.StreamListener):

    json_parser = import_simplejson()
    twat_redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    def __init__(self, search):
        super(TwatStreamListener, self).__init__()
        self.search = search

    def on_connect(self):
        print('connected!')

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)

    def on_data(self, raw_data):
        data = self.json_parser.loads(raw_data)
        time = self.to_datetime(data['timestamp_ms'])
        Postgres().insert_twat(search = self.search, text = data['text'],
            location = data['user']['location'], tweeted_at = time)
        # self.traverse(data)

    def to_datetime(self, timestamp):
        time = int(timestamp) / 1000
        return datetime.datetime.fromtimestamp(time)

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

        self.push_image_list(list(set(image_list)))

    def push_image_list(self, urls):
        if urls is list and len(urls) > 0:
            self.twat_redis.lpush('twats', *urls)
