import unittest
from unittest import TestCase
from app.api.v1.auth.models import User
import json
from app import create_app
from app.db import DatabaseConnection

class BaseClass(TestCase):
    def setUp(self):
        """
        Define test variables and initialize app
        """
        env = "testing"
        db_con = DatabaseConnection(env)
        self.app = create_app(env)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client() 
        db_con.create_users_table()

        self.user = json.dumps({
            "username" : "prossie",
            "password" : "prossie",
            "email_address" : "prossie@gmail.com"
        })

        self.missing_username = json.dumps({
            "username" : "", 
            "password" : "password", 
            "email_address" : "prossie@gmail.com"
        })

        self.missing_email = json.dumps({
            "username" : "prossie", 
            "password" : "password", 
            "email_address" : ""
        })

        self.invalid_email = json.dumps({
            "username" : "prossie", 
            "password" : "password", 
            "email_address" : "p"
        })

        self.missing_password = json.dumps({
            "username" : "prossie", 
            "password" : "", 
            "email_address" : "prossie@gmail.com"
        })

    def tearDown(self): 
        db_con = DatabaseConnection("testing")
        db_con.drop_table_data()
