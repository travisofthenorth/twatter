## Purpose

**twat** - a foolish or despicable person

This code uses the Twitter API to gather image URLs from returned tweets into Redis. The [trump tracker](http://trumptracker.travisofthenorth.com/) is an example of its usage.

## Setting up twitter streaming

Install dependencies

```bash
pip install -r requirements.txt
```

Set up Twitter API keys

```bash
export TWITTER_CONSUMER_KEY=yourkey
export TWITTER_CONSUMER_SECRET=yoursecret
export TWITTER_ACCESS_TOKEN=yourtoken
export TWITTER_ACCESS_SECRET=anothersecretyouhave
```

Install Redis on your Mac, since you're using a Mac after all

```bash
brew install redis
redis-server
```

Set up ENV vars to connect to Redis

```bash
export REDIS_HOST=localhost
export REDIS_PORT=6379
export REDIS_PASSWORD=blah
```

Optional: You can use the `data` module to dump some data into Postgres. (**The python postgres module is NOT in requirements.txt**)

```bash
createdb twatter
psql twatter < schema.sql
```

Usage

```bash
python twatter.py 'donald trump' 'kanye west' 'chicken nuggets'
```

## Setting up web server

Install Grunt, Node, etc.

1. Follow the setup instructions [here](https://github.com/peterramsing/lost/wiki/Installation#grunt)
2. Run `grunt` to compile the CSS

Run Flask

```bash
python application.py
```
