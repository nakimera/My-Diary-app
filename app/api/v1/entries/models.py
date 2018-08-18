import os
from app.db import DatabaseConnection
from app import APP_ENV

class Entry():

    def __init__(self, entry_date, title, details):
        self.entry_date  = entry_date
        self.title = title
        self.details = details
        self.db = DatabaseConnection(APP_ENV)

    def create_user_entry(self, user_id):
        """
        Method that adds a user entry to the entries table
        """

        query = f"""
                    INSERT INTO entries
                    (entry_date, title, user_id, details) 
                    values('{self.entry_date}', '{self.title}', '{user_id}', '{self.details}')
                """

        self.db.execute_query(query)
        self.db.conn.commit()
        self.db.conn.close()
    
    def fetch_user_entries(self, user_id):
        """
        Method that fetches a user's entries from the entries db
        """

        query = """
                    SELECT * 
                    FROM entries
                    WHERE user_id='{}'
                """.format(user_id)

        record = self.db.execute_query(query, fetch_all_records=True)
        entries = []

        for entry in record:
            entry_dict = {}
            entry_dict['entry_id'] = entry[0]
            entry_dict['user_id'] = entry[1]
            entry_dict['title'] = entry[2]
            entry_dict['details'] = entry[3]
            entry_dict['entry_date'] = entry[4]

            entries.append(entry_dict)

        return entries
        

    def fetch_user_entry(self, entry_id):
        """
        Method that fetches a single user entry from the entries db
        """

        query = """
                    SELECT * 
                    FROM entries
                    WHERE entry_id={}
                """.format(entry_id)

        record = self.db.execute_query(query, fetch_one_record=True)
        return record


    def modify_entries(self, entry_id):
        """
        Method that mofidies a user entry
        """

        query = f"""
                    UPDATE entries 
                    SET title = '{self.title}', details= '{self.details}'
                    WHERE entry_id={entry_id}
                """

        self.db.execute_query(query)
        self.db.conn.commit()
        self.db.conn.close()
