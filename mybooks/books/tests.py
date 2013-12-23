"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.

class SimpleTest(TestCase):
    def test_basic_addition(self):
        '''
        Tests that 1 + 1 always equals 2.
        '''
        self.assertEqual(1 + 1, 2)
"""

from django.test import TestCase
from .models import *
import datetime

class TestBook(TestCase):
	def test_horror_manager(self):
		'''
		Tests if the horror manager is functioning as
		intended.
		'''
		random_author=Author(name="Stephen King", origin="USA")
		random_author.save()
		random_book = Book(isbn="29489461", genre="horror", name="Rage",\
		   language="English", author=random_author,\
		   date_of_publish=datetime.date(day=10,month=9,year=1977),\
		   summary="Random shit", no_of_pages=320, publisher="pubby")
		random_book.save()
		
		self.assertEqual(Book.horror.get(name="Rage").author.name, "Stephen King")
		self.assertEqual(Book.horror.get(no_of_pages=320).name, "Rage")
		
		#self.assert()

