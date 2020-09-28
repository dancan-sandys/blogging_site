import unittest
from app.models import Comment,User
from app import db

class test_comment(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username = 'Dancan',email ='sandys@gmail.com',password = 'Stanford2020*')
        self.new_comment = Comment(title = 'Great', body = 'Even greater')

    def tearDown(self):
        User.query.delete()
        Comment.query.delete()

    def test_instance(self):

        self.assertTrue(isinstance(self.new_comment , Comment))

    def test_save_comment(self):

        self.new_comment.save_comment()
        self.assertEqual(len(Comment.query.all()), 1)

    def test_delete_comment(self):

        self.new_comment.save_comment()
        self.assertEqual(len(Comment.query.all()),1)
        self.new_comment.delete_comment()
        self.assertEqual(len(Comment.query.all()),0)
















