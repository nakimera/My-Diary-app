from app.db import DatabaseConnection


class Entry(DatabaseConnection):

    def __init__(self, entry_date, title, details):
        self.entry_date  = entry_date
        self.title = title
        self.details = details

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

        record = self.execute_query(query, fetch_one_record=True)
        # return record
    
        entry = {}
        entry['entry_id'] = record[0]
        entry['user_id'] = record[1]
        entry['title'] = record[2]
        entry['details'] = record[3]
        entry['entry_date'] = record[4]

        return entry

        
    def modify_entries(self, title, description, entry_id):
        """
        Method that mofidies a user entry
        """

        query = """
                    UPDATE entries SET title = ''  WHERE entry_id={}
                """.format(entry_id)

        return ''
