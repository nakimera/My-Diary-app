from tests.test_base import BaseClass

class EntryTests(BaseClass):
    """This class represents the Entrytest case"""

    # Test api can not add an entry without a token
    def test_create_entry(self):
        response = self.client.post('/api/v1/entries', data=self.entry)
        self.assertEqual(response.status_code, 403)
        self.assertIn('Token is missing', str(response.data))

    # Test api can not add entry with invalid token
    def test_invalid_token(self):
        response = self.client.post('/api/v1/entries', data=self.entry)
        # self.assertEqual(response.status_code, 403)
        self.assertIn('Invalid Token', str(response.data))