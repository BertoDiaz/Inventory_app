from django.db import models
from django.utils import timezone


class Element(models.Model):
    author = models.ForeignKey('auth.User')
    type_item = models.ForeignKey('Type')
    name = models.CharField(max_length=200)
    maker = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Type(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
