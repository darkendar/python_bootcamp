from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to="books_covers/%Y/%m/%d")

    def __str__(self):
        return f"{self.title} - {self.author}"

# Create your models here.
