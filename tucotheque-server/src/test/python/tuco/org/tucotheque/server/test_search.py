'''
Created on 22 nov. 2018

@author: tuco
'''
import unittest

from tuco.org.tucotheque.server.app import app
import json


class TestSearch(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def testBarcodeSearch(self):
        response = self.app.get('/search?barcode=3218030139592')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data), {'results': [{'source': 'discogs', 'id': 534319}]}, 'Service output wrong')


if __name__ == "__main__":
    unittest.main()