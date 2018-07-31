import psycopg2
from app.config import DevelopmentConfig

class Connection:

    def __init__(self):
        self.conn = psycopg2.connect(DevelopmentConfig.DATABASE_URL)

    def execute_query(self, query):
        """
        This method executes a query in the database
        """

        try:
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()

        except psycopg2.DatabaseError as ex:
            self.conn.close()
            print(ex)

    def close_connection(self):
        """
        This method closes the database
        """
        self.conn.close()