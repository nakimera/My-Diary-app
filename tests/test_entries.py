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
        # self.assertIn('{}'.format(self.), str(response.data))
        
    # Test api can fetch all user entries
    def test_get_entries(self):
        self.client.post(
            '/api/v1/entries', data=self.entry,
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        self.client.post(
            '/api/v1/entries', data=self.entry1, 
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        response = self.client.get(
            '/api/v1/entries',
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('All entries successfully retrieved', str(response.data))
        # self.assertIn('{}'.format(self.entry), str(response.data))
        
    # Test api can fetch a single user entry
    def test_get_entry_by_id(self):
        self.client.post(
            '/api/v1/entries', data=self.entry,
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        self.client.post(
            '/api/v1/entries', data=self.entry1, 
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        response = self.client.get(
            '/api/v1/entries/2',
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Entry successfully retrieved', str(response.data))

    # Test api can not fetch a single user entry with an invalid entry id
    def test_invalid_entry_id(self):
        self.client.post(
            '/api/v1/entries', data=self.entry,
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        response = self.client.get(
            '/api/v1/entries/2',
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        self.assertEqual(response.status_code, 404)
        self.assertIn('Entry does not exist. Try again', str(response.data))

    # Test api can modify a user entry
    def test_modify_user_entry(self):
        self.client.post(
            '/api/v1/entries', data=self.entry,
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        response = self.client.put(
            '/api/v1/entries/1', data=self.entry1,
            content_type="application/json", 
            headers={ "access-token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Entry successfully updated', str(response.data))