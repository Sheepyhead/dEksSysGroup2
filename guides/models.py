from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Guide(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey(Category)
    def __str__(self):
        return self.title
