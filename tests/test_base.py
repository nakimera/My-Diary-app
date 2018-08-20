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
        db_con.create_entries_table()

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

        self.entry = json.dumps({
            "title" : "Living in Kabojja",
            "details" : "It takes alot"
        })

        self.entry1 = json.dumps({
            "title" : "Andela Bootcamp",
            "details" : "The struggle continues"
        })

        self.missing_title = json.dumps({
            "title" : "",
            "details" : "some details"
        })

        self.missing_details = json.dumps({
            "title" : "some title",
            "details" : ""
        })

        self.reigister = self.client.post(
            '/api/v1/auth/signup', 
            data=self.user,
            content_type="application/json"
        )

        self.login = self.client.post(
            '/api/v1/auth/login', 
            data=self.user,
            content_type="application/json"
        )

        self.token = json.loads(self.login.data.decode())["token"]

    def tearDown(self): 
        db_con = DatabaseConnection("testing")
        db_con.drop_table_data()
