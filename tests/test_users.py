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
    