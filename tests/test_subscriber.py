import unittest
from app.models import Subscriber
from app import db


class test_subscriber(unittest.TestCase):

    def setUp(self):
        self.new_subscriber = Subscriber(email ='Sandys@gmail.com')

    def tearDown(self):
        Subscriber.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_subscriber,Subscriber))

    def test_save_subscriber(self):
        self.new_subscriber.save_subscriber()
        self.assertTrue(len(Subscriber.query.all()),1)