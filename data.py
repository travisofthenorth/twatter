import psycopg2

class Postgres:
    class __Postgres:
        connection = psycopg2.connect("dbname=twatter user=travis")

        def insert_twat(self, text, location, search, tweeted_at):
          cursor = self.connection.cursor()
          cursor.execute("""INSERT INTO twats (text, location, search, tweeted_at)
            VALUES (%s, %s, %s, %s);""",
            (text, location, search, tweeted_at)
          )
          self.connection.commit()

    instance = None

    def __init__(self):
        if not Postgres.instance:
            Postgres.instance = Postgres.__Postgres()

    def __getattr__(self, name):
        return getattr(self.instance, name)
