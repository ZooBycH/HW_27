from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=450)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
