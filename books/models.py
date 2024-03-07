from django.db import models
# from django.db.models.base import ModelState
from django.contrib.auth.models import User
from django.db.models import CharField
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> CharField:
        return self.name


def upload_to(instance, filename):
    return 'book_files/{0}/{1}'.format(instance.title, filename)


class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    shortDescription = models.CharField(max_length=256, null=True)
    authors = models.ManyToManyField(Author)
    book_file = models.FileField(upload_to=upload_to, null=True, blank=True)
    image = models.ImageField(default='book_image/book_image.jpg', upload_to='media')
    create_at = models.DateField(auto_now=True)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        if len(self.body) > 20:
            return self.body[:20] + '...'
        else:
            return self.body

    class Meta:
        db_table = 'review_table'

