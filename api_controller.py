import random
import redis
from flask import Flask, render_template, jsonify, send_from_directory

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

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('assets/dist/css', path)

if __name__ == "__main__":
    app.debug = True
    app.run()
