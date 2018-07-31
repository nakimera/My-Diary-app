import psycopg2

class Connection:

    def __init__(self):
        self.conn = psycopg2.connect(URL)

    def execute_query(self):
        """
        This method executes a query in the database
        """

        try:
            cur = self.conn.cursor()
            cur.execute(query)

        except psycopg2.DatabaseError as ex:
            self.conn.close()

    def close_connection(self):
        """
        This method closes the database
        """
        self.conn.close()