import json

from tests.test_base import BaseClass


class EntryTests(BaseClass):
    """This class represents the Entrytest case"""

    # authourization
    def auth(self):
            self.client.post('/api/v1/auth/signup', data=self.user)
            response = self.client.post('/api/v1/auth/login', data=self.user)
            token = json.loads(response.data.decode())["token"]
            return token 

    # Test api can not add an entry without a token
    def test_create_entry(self):
        response = self.client.post('/api/v1/entries', data=self.entry, content_type="application/json")
        self.assertEqual(response.status_code, 403)
        self.assertIn('Token is missing', str(response.data))

    # Test api can not add entry with invalid token
    def test_invalid_token(self):
        token = "some random token"
        response = self.client.post(
            '/api/v1/entries', data=self.entry, 
            content_type="application/json", 
            headers={ "access-token": token
        })
        # self.assertEqual(response.status_code, 403)
        self.assertIn('Invalid token. Please try again.', str(response.data))
