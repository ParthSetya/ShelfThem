from django.contrib import admin
from django import forms
from django.db import models
from .models import Book, Author

class AuthorAdmin(admin.ModelAdmin):
	list_display = ("name", "origin")

class BookAdmin(admin.ModelAdmin):
	list_display = ("name", "isbn", "genre", "language", "author", "no_of_pages")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)