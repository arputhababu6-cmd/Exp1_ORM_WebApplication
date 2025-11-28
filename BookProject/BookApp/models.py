from django.db import models
from django.contrib import admin

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'isbn_number']
    