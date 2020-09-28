import unittest
from app.models import User
from app import db

class test_user(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username = 'Dancan',email ='sandys@gmail.com',password = 'Stanford2020*')

    def tearDown(self):
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.query.all()),1)






























