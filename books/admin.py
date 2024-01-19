from django.contrib import admin
from .models import Book, Review, Author
from django.contrib.admin import ModelAdmin


# Register your models here.

class BooksUathorModel(admin.ModelAdmin):
    search_fields = ['title', 'name']


admin.site.register(Book, BooksUathorModel)
admin.site.register(Review)
admin.site.register(Author, BooksUathorModel)
