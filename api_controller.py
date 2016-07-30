import random
import redis
# from data import Postgres

from flask import Flask, render_template, jsonify
app = Flask(__name__)
twat_redis = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route("/")
def home():
    return render_template('twatimg.html', data=twat_redis.hgetall('twatter_image'))

@app.route("/latest_trump")
def latest_trump():
  return jsonify(twat_redis.hgetall('twatter_image'))

@app.route("/counts")
def counts():
    results = Postgres().count_twats()
    results = sorted(results, key=lambda result: result[1])
    return render_template('counts.html', results=results)

if __name__ == "__main__":
    app.debug = True
    app.run()
