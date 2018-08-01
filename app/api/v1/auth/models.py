from app.db import DatabaseConnection

class User(DatabaseConnection):
    """
    This class defines the app users
    """

    def __init__(self, username, email_address, password):
        DatabaseConnection.__init__(self)
        self.username = username
        self.email_address = email_address
        self.password = password

    def create_user(self):
        self.add_user()

    def login_user(self):
        self.fetch_user()

    def add_user(self):
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

    # def get_user(username):
        