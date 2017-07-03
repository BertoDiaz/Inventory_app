from django.db import models
from django.utils import timezone

""" Models Inventory """


class Element(models.Model):
    """docstring for Element."""

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
    """docstring for Type."""

    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


""" ------------------------------ """


""" Models Order """


class Order(models.Model):
    """docstring for Order."""

    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    research = models.CharField(max_length=200)
    budget = models.ForeignKey('Budget')
    buy_type = models.ForeignKey('Buy_Type')
    payment_requirements = models.ForeignKey('Payment')
    provider = models.ForeignKey('Provider')
    # product = models.ForeignKey('Product', null=True)
    number_product = models.IntegerField(default=1)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Budget(models.Model):
    """docstring for Budget."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Buy_Type(models.Model):
    """docstring for Buy_Type."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Payment(models.Model):
    """docstring for Payment."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Provider(models.Model):
    """docstring for Provider."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Product(models.Model):
    """docstring for Product."""

    description = models.CharField(max_length=300)
    quantity = models.CharField(max_length=20)
    unit_price = models.CharField(max_length=20)
    order = models.ForeignKey('Order', null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.description


""" ------------------------------ """
