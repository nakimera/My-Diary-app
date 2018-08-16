import json

from tests.test_base import BaseClass


class EntryTests(BaseClass):
    """This class represents the Entrytest case"""

    # Test api can not add an entry without a token
    def test_missing_token(self):
        response = self.client.post(
            '/api/v1/entries', 
            data=self.entry, 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 403)
        self.assertIn('Token is missing', str(response.data))

    # Test api can not add entry with invalid token
    def test_invalid_token(self):
        self.token = "some random token"
        response = self.client.post(
            '/api/v1/entries', data=self.entry, 
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        self.assertEqual(response.status_code, 403)
        self.assertIn('Invalid token. Please try again.', str(response.data))

    # Test api cannot add an entry with missing title
    def test_entry_title(self):
        response = self.client.post(
            '/api/v1/entries', data=self.missing_title, 
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please enter a title', str(response.data))

        # Test api cannot add an entry with missing details
    def test_entry_details(self):
        response = self.client.post(
            '/api/v1/entries', data=self.missing_details, 
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please enter details', str(response.data))
        

    # Test api can successfully add an entry
    def test_add_entry(self):
        response = self.client.post(
            '/api/v1/entries', data=self.entry, 
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Entry successfully added', str(response.data))
        