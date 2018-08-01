import unittest
from unittest import TestCase
from app.api.v1.auth.models import User
import json
from app import create_app

class UserTests(TestCase):
    """This class represents the User test case"""

    def setUp(self):
        """
        Define test variables and initialize app
        """

        self.app = create_app("testing")
        self.client = self.app.test_client
        self.user = {
            "username" : "prossie",
            "password" : "password",
            "email_address" : "prossie@gmail.com"
        }   

    # Test api can create a user
    def test_create_user(self):
        response = self.client().post('/api/v1/auth/signup', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 201)
        self.assertIn('User successfully signed up', str(response.data))

    # Test api can not create a user without a username
    def test_cannot_create_user_without_username(self):
        self.user = {"username" : "", "password" : "password", "email_address" : "prossie@gmail.com"}
        response = self.client().post('/api/v1/auth/signup', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please provide a username', str(response.data))

    # Test api can not create a user without an email address
    def test_cannot_create_user_without_email(self):
        pass
    
    # Test api can not create a user without a password
    def test_cannot_create_user_without_password(self):
        pass

    # Test api can not create a user that already exists
    def test_cannot_create_an_existing_user(self):
        pass