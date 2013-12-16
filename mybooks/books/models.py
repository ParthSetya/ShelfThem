from django.db import models

class Author(models.Model):
	name = models.TextField()
	origin = models.TextField()

class ISBNManager(models.Manager):
	def __init__(self,isbn):
		self.isbn=isbn

	def get_query_set(self):
		return super(ISBNManager, self).get_query_set().filter(isbn=self.isbn)


class Book(models.Model):
	'''
	This model contains all the information about a book. This
	information may be the book's metadata or external information
	added by users.
	'''
	isbn = models.TextField()
	genre = models.TextField()
	name = models.TextField()
	language = models.TextField()
	author = models.ForeignKey(Author)
	date_of_publish = models.DateField()
	summary = models.TextField()
	no_of_pages = models.IntegerField()
	publisher = models.TextField()
	#cover_image - Upload an Image of the cover
	#no_of_reviews - number of views on the book by people
	#average_rating - number of stars(x/5)

