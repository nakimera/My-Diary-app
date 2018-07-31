import psycopg2

class Connection:

    def __init__(self):
        self.conn = psycopg2.connect(URL)

    def execute_query(self):
        """
        This method executes a query inthe database
        """

        try:
            cur = self.conn.cursor()
            cur.execute(query)

        except psycopg2.DatabaseError as ex:
            self.conn.close()

    def close_connection(self):
        """
        This method closes the database connection
        """
        self.conn.close()

class User(Connection):
    """
    This class defines the app users
    """

    def __init__(self, username, email_address, password):
        self.username = username
        self.email_address = email_address
        self.password = password

    def add_user(self):

        return ''

    @staticmethod
    def user_login(username, password):
        return ''