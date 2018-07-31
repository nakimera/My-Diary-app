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

        query = """
                    CREATE TABLE IF NOT EXISTS users
                    (user_id SERIAL PRIMARY KEY,
                    username VARCHAR(30) NOT NULL UNIQUE,
                    email_address VARCHAR(50) UNIQUE NOT NULL,
                    password)
                """
        
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()

        except:
            psycopg2.DatabaseError as ex:
            print(ex)
        
        finally:
            self.conn.close()


    def add_user(self):
        """
        Method that adds a user to the users table
        """

        query = f"""
                    INSERT INTO users
                    (username, email_address, password) 
                    values('{username}', '{email_address}', '{password}')"
                """

        try:
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()

        except:
            psycopg2.DatabaseError as ex:
            print(ex)
        
        finally:
            self.conn.close()

    def fetch_user(self):
        """
        Method that fetches a user from the DB
        """

        query = """
                    SELECT * 
                    FROM users 
                    WHERE username='{}'
                """.format(username)

        try:
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()

        except:
            psycopg2.DatabaseError as ex:
            print(ex)
        
        finally:
            self.conn.close()