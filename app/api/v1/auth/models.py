from app.db import Connection

class User(Connection):
    """
    This class defines the app users
    """

    def __init__(self, username, email_address, password):
        Connection.__init__(self)
        self.username = username
        self.email_address = email_address
        self.password = password

    def add_user(self):
        query = f"""insert into users(username, email_address, password) 
        values('{self.username}', '{self.email_address}', '{self.password}')"""
        self.execute_query(query)
        self.close_connection()

    @staticmethod
    def user_login(username, password):
        return ''