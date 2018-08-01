import psycopg2
from app.config import DevelopmentConfig

class DatabaseConnection:
    """
    Class to setup a database connection 
    """

    def __init__(self):
        self.conn = None

    def execute_query(self, query, fetch_one_record=False, fetch_all_records=False):

        try:
            self.conn = psycopg2.connect(DevelopmentConfig.DATABASE_URL)
            cur = self.conn.cursor()
            cur.execute(query)

            if fetch_one_record:
                return cur.fetchone()


            if fetch_all_records:
                return cur.fetchall()
            cur.close()

        except psycopg2.DatabaseError as ex:
            print(ex)     

    def create_users_table(self):
        """
        Method that creates the users table if it doesn't exist
        """

        query = """
                    CREATE TABLE IF NOT EXISTS users
                    (user_id SERIAL PRIMARY KEY,
                    username VARCHAR(30) NOT NULL UNIQUE,
                    email_address VARCHAR(50) UNIQUE NOT NULL,
                    password)
                """

        self.execute_query(query)
        self.conn.commit()
        self.conn.close()

    