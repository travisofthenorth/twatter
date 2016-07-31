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
```

Optional: Set up database (assuming postgres is installed). You should checkout the tag `text`, which actually dumps some data into Postgres.

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
python api_controller.py
```
