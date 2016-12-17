import os
import random
import redis
from flask import Flask, render_template, jsonify, send_from_directory

application = Flask(__name__)
twit_redis = redis.StrictRedis(
    host=os.environ['REDIS_HOST'],
    port=os.environ['REDIS_PORT'],
    password=os.environ['REDIS_PASSWORD']
)

@application.route("/")
def home():
    return render_template('twitimg.html', data=twit_redis.hgetall('twitter_image'))

@application.route("/latest_trump")
def latest_trump():
  return jsonify(twit_redis.hgetall('twitter_image'))

@application.route("/counts")
def counts():
    results = Postgres().count_twits()
    results = sorted(results, key=lambda result: result[1])
    return render_template('counts.html', results=results)

@application.route("/static/<path:path>")
def send_css(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    application.run()
