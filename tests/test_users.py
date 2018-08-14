import unittest
from unittest import TestCase
from app.api.v1.auth.models import User
import json
from app import create_app
from app.db import DatabaseConnection

class UserTests(TestCase):
    """This class represents the User test case"""

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

        self.user = {
            "username" : "serryjk",
            "password" : "johnzjk",
            "email_address" : "serembaj@gmail.com"
        }

    def tearDown(self): 
        db_con = DatabaseConnection("testing")
        db_con.drop_table_data()

    # Test api can create a user
    def test_create_user(self):
        with self.client:
            response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user))
            self.assertEqual(response.status_code, 201)
            self.assertIn('User successfully signed up', str(response.data))


    # Test api can not create a user without a username
    def test_cannot_create_user_without_username(self):
        self.user = {
                        "username" : "", 
                        "password" : "password", 
                        "email_address" : "prossie@gmail.com"
                    }
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide a username", str(response.data))


    # Test api can not create a user without an email address
    def test_cannot_create_user_without_email(self):
        self.user = {
                        "username" : "prossie", 
                        "password" : "password", 
                        "email_address" : ""
                    }
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide an email address", str(response.data))

    # Test api can not create a user without an invalid email address
    def test_cannot_create_user_with_an_invalid_email(self):
        self.user = {
                        "username" : "prossie", 
                        "password" : "password", 
                        "email_address" : "p"
                    }
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide a valid email address", str(response.data))
    
    # Test api can not create a user without a password
    def test_cannot_create_user_without_password(self):
        self.user = {
                        "username" : "prossie", 
                        "password" : "", 
                        "email_address" : "prossie@gmail.com"
                    }
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide a password", str(response.data))

    # Test api can not create a user that already exists
    def test_cannot_create_an_existing_user(self): 
        self.client.post('/api/v1/auth/signup', data=json.dumps(self.user))
        response = self.client.post('/api/v1/auth/signup', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 409)
        self.assertIn("User already exists. Please log in", str(response.data))


    # Test user can not login without a username
    def test_user_can_not_log_in_without_username(self):
        self.user = {
                        "username" : "", 
                        "password" : "password"
                    }
        response = self.client.post('/api/v1/auth/login', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide a username", str(response.data))


    # Test user can not login without a password
    def test_user_can_not_log_in_without_password(self):
        self.user = {
                        "username" : "username", 
                        "password" : ""
                    }
        response = self.client.post('/api/v1/auth/login', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide a password", str(response.data))


    # Test api can log in a user and generate a token
    def test_user_can_log_in(self):
        self.client.post('/api/v1/auth/signup', data=json.dumps(self.user))
        response = self.client.post('/api/v1/auth/login', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 200)
        self.assertIn("You have successfully logged in", str(response.data))
        token = json.loads(response.data.decode())["token"]
        self.assertIn(token, str(response.data))

    