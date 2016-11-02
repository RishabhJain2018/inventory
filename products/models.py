from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    # status = models.IntegerField()


# class Stat(models.Model):
#     Category_count = models.IntegerField()


# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     category = models.ForeignKey(Category)
