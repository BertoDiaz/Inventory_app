from django.db import models
from django.utils import timezone


class Inventory(models.Model):
    """docstring for Inventory."""
    author = models.ForeignKey('User')
    name = models.CharField(max_length=200)
    maker = models.CharField(max_length=200)
    type_item = models.ForeignKey('Type')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class User(models.Model):
    """docstring for Users."""
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str(self):
        return self.name


class Type(models.Model):
    """docstring for Types."""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
