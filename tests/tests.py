import unittest
from flask import jsonify
from app import models


class testing_models(unittest.TestCase):
    """books testing class"""
    def setUp(self):
        self.user = models.User()
        self.bookie = models.Books()


    def test_add_book(self):
        result = self.bookie.add_book('Paradise', 'Fantasy', 'Dreams of a happy soul in a happy place', 1)
        self.assertIn('Paradise', result['title'])
if __name__=='__main__':
    unittest.main()
