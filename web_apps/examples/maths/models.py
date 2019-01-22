from django.db import models

# Create your models here.


class Math(models.Model):

    operacja = models.CharField(max_length=4)
    a = models.IntegerField()
    b = models.IntegerField()
    wynik = models.TextField()
    created = models.DateTimeField(auto_now=True)
