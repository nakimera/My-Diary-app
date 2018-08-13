import unittest
from unittest import TestCase
from app.api.v1.entries.models import Entry
import json
from app import create_app
from app.db import DatabaseConnection

class EntryTests(TestCase):
    """This class represents the Entrytest case"""

    def setUp(self):
        """
        Define test variables and initialize app
        """

        db_con = DatabaseConnection()
        db_con.drop_table_data()
        self.app = create_app("testing")
        self.client = self.app.test_client  
        db_con.create_entries_table()


    # Test api can add an entry
    def test_create_entry(self):
        self.entry = {
            "details": "Living in Kabojja",
            "title": "Wakanda"
        }
        response = self.client().post('/api/v1/entries', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 201)
        self.assertIn('User successfully signed up', str(response.data))
