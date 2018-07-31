import psycopg2
from app.config import DevelopmentConfig

class DatabaseConnection:
    """
    Class to setup a database connection 
    """

    def __init__(self):
        self.conn = psycopg2.connect(DevelopmentConfig.DATABASE_URL)        

    def create_users_table(self):
        """
        Method that creates the users table if it doesn't exist
        """
        query = """CREATE TABLE IF NOT EXISTS users
                    (user_id SERIAL PRIMARY KEY,
                    username VARCHAR(30) NOT NULL UNIQUE,
                    email_address VARCHAR(50) UNIQUE NOT NULL,
                    password)
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