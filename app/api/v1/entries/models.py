from app.db import DatabaseConnection

class Entry(DatabaseConnection):

    def __init__(self, entry_date, title, details):
        self.entry_date  = entry_date
        self.title = title
        self.details = details

    # Method to add a  user entry
    def create_user_entry(self, user_id):
        """
        Method that adds a user entry to the entries table
        """

        query = f"""
                    INSERT INTO entries
                    (entry_date, title, user_id, details) 
                    values('{self.entry_date}', '{self.title}', '{user_id}', '{self.details}')
                """

        self.execute_query(query)
        self.conn.commit()
        self.conn.close()

    # Method to fetch a user's entries
    def fetch_user_entries(self, user_id):
        """
        Method that fetches a user's entries from the entries db
        """

        query = """
                    SELECT * 
                    FROM entries
                    WHERE user_id='{}'
                """.format(user_id)

        record = self.execute_query(query, fetch_all_records=True)
        return record
        
        self.conn.close()

    def modify_entries(title, description):
        return ''

    def get_entry(entry_id):
        return ''