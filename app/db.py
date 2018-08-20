import psycopg2
import os

from app.config import app_config


class DatabaseConnection:
    """
    Class to setup a database connection 
    """

    def __init__(self, environment):
        self.conn = None
        self.environment = environment

    def execute_query(self, query, fetch_one_record=False, fetch_all_records=False):

        try:
            self.conn = psycopg2.connect(app_config[self.environment].DATABASE_URL)
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
                    title VARCHAR(50) NOT NULL,
                    details VARCHAR NOT NULL,
                    entry_date DATE NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users (user_id))
                """

        self.execute_query(query)
        self.conn.commit()
        self.conn.close()

    def drop_table_data(self):
        """
        Method that drops tables
        """
        query = ("DROP TABLE users, entries")
        self.execute_query(query)
        self.conn.commit()
        self.conn.close()

