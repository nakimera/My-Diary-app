from app.db import DatabaseConnection

class User(DatabaseConnection):
    """
    This class defines the app users
    """

    def __init__(self, username, password, email_address):
        DatabaseConnection.__init__(self)
        self.username = username
        self.email_address = email_address
        self.password = password

    def create_user(self):
        self.add_user()

    def login_user(self):
        self.fetch_user()
        