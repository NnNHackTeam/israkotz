from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

class City(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)