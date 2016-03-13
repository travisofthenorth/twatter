import random
from data import Postgres

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def counts():
    results = Postgres().count_twats()
    results = sorted(results, key=lambda result: result[1])
    return render_template('counts.html', results=results)

if __name__ == "__main__":
    app.debug = True
    app.run()
