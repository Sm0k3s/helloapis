import unittest

from app import models, data

class testing_models(unittest.TestCase):
    """books testing class"""
    def setUp(self):
        self.my_book = Books()


    def test_add_book(self):
        self.my_book.put('Paradise','Fantasy','Dreams of a happy soul in a happy place')
        self.assertIn('Paradise', books[-1])

if __name__=='__main__':
    unittest.main()
