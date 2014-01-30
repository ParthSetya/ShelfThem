from django.db import models
from django.contrib.auth.models import User

class Reader(models.Model):
	user=models.OneToOneField(User)
	books_read=models.TextField(default=0, blank=True)
	books_want_to_read=models.TextField(default=0, blank=True)
	books_reading=models.TextField(default=0, blank=True)	


class Author(models.Model):
	name = models.TextField()
	origin = models.TextField()

class HorrorManager(models.Manager):

	def get_query_set(self):
		return super(HorrorManager, self).get_query_set().filter(genre="horror")


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
	horror=HorrorManager()
	#cover_image - Upload an Image of the cover
	#no_of_reviews - number of views on the book by people
	#average_rating - number of stars(x/5)


