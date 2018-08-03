from flask import jsonify
import datetime
import jwt
from app.db import DatabaseConnection
from app.config import Config

class User(DatabaseConnection):
    """
    Model for the app users
    """

    def __init__(self, username, email_address, password):
        DatabaseConnection.__init__(self)
        self.username = username
        self.email_address = email_address
        self.password = password

    def create_user(self):
        """
        Method that adds a user to the users table
        """

        query = f"""
                    INSERT INTO users
                    (username, email_address, password) 
                    values('{self.username}', '{self.email_address}', '{self.password}')
                """

        self.execute_query(query)
        self.conn.commit()
        self.conn.close()

    def fetch_user(self, email_address):
        """
        Method that fetches a user from the DB
        """

        query = """
                    SELECT * 
                    FROM users 
                    WHERE email_address='{}'
                """.format(email_address)

        record = self.execute_query(query,fetch_one_record=True)
        return record
        
        self.conn.close()

    def encode_auth_token(self, user_id):
        """
        Method that encodes authentication token
        """

        try:
            payload = {
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=20),
                'iat' : datetime.datetime.utcnow(),
                'sub' : user_id
            }
            return jwt.encode(
                payload,
                Config.SECRET_KEY,
                algorithm='HS256'
            )

        except Exception as ex:
            return ex

            
