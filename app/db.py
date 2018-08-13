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
                cur.close()

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
                    password VARCHAR(150) NOT NULL)
                """

        self.execute_query(query)
        self.conn.commit()
        self.conn.close()

    def create_entries_table(self):
        """
        Method that creates the entries table if it doesn't exist
        """
        query = """
                    CREATE TABLE IF NOT EXISTS entries
                    (entry_id SERIAL PRIMARY KEY,
                    user_id INTEGER,
                    title VARCHAR(50) UNIQUE NOT NULL,
                    details VARCHAR NOT NULL,
                    entry_date DATE NOT NULL,
                    date_modified DATE,
                    FOREIGN KEY(user_id) REFERENCES users (user_id))
                """

        self.execute_query(query)
        self.conn.commit()
        self.conn.close()

    def drop_table_data(self):
        """
        Method that drops tables
        """
        query = ("DROP TABLE users CASCADE ")
        self.execute_query(query)
        query2 = ("DROP TABLE entries CASCADE ")
        self.execute_query(query2)
        self.conn.commit()
        self.conn.close()

