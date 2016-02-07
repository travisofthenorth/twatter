## Setting up

Install dependencies

```bash
pip install tweepy
pip install redis
pip install psycopg2
```

Set up database (assuming postgres is installed)

```bash
createdb twatter
psql twatter < schema.sql
```

Usage

```bash
python twatter.py 'donald trump' 'kanye west' 'chicken nuggets'
```
