class Entry(object):
    """
    This class defines the entry model
    """

    def __init__(self, entry_date, title, details):
        self.title = title
        self.entry_date = entry_date
        self.details = details

    # Method to add a  user entry
    def create_user_entry(self):
        """
        Method that adds a user entry to the entries table
        """

        query = f"""
                    INSERT INTO entries
                    (entry_date, title, user_id, details) 
                    values('{self.entry_date}', '{self.title}', '{self.user_id}', '{self.details}')
                """

        self.execute_query(query)
        self.conn.commit()
        self.conn.close()

    def modify_entries(title, description):
        return ''

    def get_entry(entry_id):
        return ''