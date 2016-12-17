import os
import psycopg2

class Postgres:
    class __Postgres:
        connection = psycopg2.connect(host=os.environ.get('PG_HOST', 'localhost'),
          user=os.environ['PG_USER'], password=os.environ.get('PG_PASSWORD', None),
          dbname=os.environ.get('PG_DBNAME', 'twedis'), port=os.environ.get('PG_PORT', 5432),
        )

        def insert_twit(self, text, location, search, tweeted_at):
          cursor = self.connection.cursor()
          cursor.execute("""INSERT INTO twits (text, location, search, tweeted_at)
            VALUES (%s, %s, %s, %s);""",
            (text, location, search, tweeted_at)
          )
          self.connection.commit()

        def count_twits(self):
          cursor = self.connection.cursor()
          cursor.execute("select count(*), search from twits group by search;")
          return cursor.fetchall()

    instance = None

    def __init__(self):
        if not Postgres.instance:
            Postgres.instance = Postgres.__Postgres()

    def __getattr__(self, name):
        return getattr(self.instance, name)
