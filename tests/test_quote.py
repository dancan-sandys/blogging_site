import unittest
from app.models import Quotes
from app import db

class test_quote(unittest.TestCase):

    def setUp(self):
        self.new_quote = Quotes(author = 'Dancan', quote = 'For every problem ther is a solution')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote, Quotes))