import unittest
from app.models import Blogs
from app import db

class test_blog(unittest.TestCase):

    def setUp(self):
        self.new_blog = Blogs(title ='Sereni', body = 'I got you')

    def tearDown(self):
        Blogs.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blogs))

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertEqual(len(Blogs.query.all()),1)

    def test_delete_blog(self):
        self.new_blog.save_blog()
        self.assertEqual(len(Blogs.query.all()),1)
        self.new_blog.delete_blog()
        self.assertEqual(len(Blogs.query.all()),0)