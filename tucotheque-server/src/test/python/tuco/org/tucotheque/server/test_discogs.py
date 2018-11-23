'''
Created on 22 nov. 2018

@author: tuco
'''
import unittest

from tuco.org.tucotheque.server.app import app


class TestDiscogs(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def testReleaseGet(self):
        response = self.app.get('/discogs/release/%d' % 534319)
        self.assertEqual(response.status_code, 200)
