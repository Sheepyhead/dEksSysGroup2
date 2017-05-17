from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class GuideSuggestion(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    def __str__(self):
        return self.name



class Guide(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100, default="")
    text = models.TextField()
    category = models.ForeignKey(Category)
    subcategory = models.CharField(max_length=20, default="General")
    author = models.CharField(max_length=20, default="Anonymous")

    def __str__(self):
        return self.title
