from tests.test_base import BaseClass
import json

class UserTests(BaseClass):
    """This class represents the User test case"""

    # Test api can create a user
    def test_create_user(self):
        response = self.client.post(
            '/api/v1/auth/signup', 
            data=self.user, 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('User successfully signed up', str(response.data))


    # Test api can not create a user without a username
    def test_cannot_create_user_without_username(self):
        response = self.client.post(
            '/api/v1/auth/signup', 
            data=self.missing_username, 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide a username", str(response.data))


    # Test api can not create a user without an email address
    def test_cannot_create_user_without_email(self):
        response = self.client.post(
            '/api/v1/auth/signup', 
            data=self.missing_email, 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide an email address", str(response.data))

    # Test api can not create a user without an invalid email address
    def test_cannot_create_user_with_an_invalid_email(self):
        response = self.client.post(
            '/api/v1/auth/signup', 
            data=self.invalid_email,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide a valid email address", str(response.data))
    
    # # Test api can not create a user without a password
    def test_cannot_create_user_without_password(self):
        response = self.client.post(
            '/api/v1/auth/signup', 
            data=self.missing_password,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide a password", str(response.data))

    # # Test api can not create a user that already exists
    def test_cannot_create_an_existing_user(self): 
        self.client.post(
            '/api/v1/auth/signup', 
            data=self.user,
            content_type="application/json"
        )
        response = self.client.post('/api/v1/auth/signup', data=self.user)
        self.assertEqual(response.status_code, 409)
        self.assertIn("User already exists. Please log in", str(response.data))


    # # Test user can not login without a username
    def test_user_can_not_log_in_without_username(self):
        response = self.client.post(
            '/api/v1/auth/login', 
            data=self.missing_username,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide a username", str(response.data))


    # # Test user can not login without a password
    def test_user_can_not_log_in_without_password(self):
        response = self.client.post(
            '/api/v1/auth/login', 
            data=self.missing_password,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please provide a password", str(response.data))


    # # Test api can log in a user and generate a token
    def test_user_can_log_in(self):
        self.client.post(
            '/api/v1/auth/signup', 
            data=self.user,
            content_type="application/json"
        )
        response = self.client.post(
            '/api/v1/auth/login', 
            data=self.user,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("You have successfully logged in", str(response.data))
        token = json.loads(response.data.decode())["token"]
        self.assertIn(token, str(response.data))

    