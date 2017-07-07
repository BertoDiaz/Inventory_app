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
    applicant = models.CharField(max_length=200)
    budget = models.ForeignKey('Budget')
    type_of_purchase = models.ForeignKey('Type_of_purchase')
    payment_conditions = models.ForeignKey('Payment')
    supplier = models.ForeignKey('Supplier')
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


class Type_of_purchase(models.Model):
    """docstring for Type_of_purchase."""

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


class Supplier(models.Model):
    """docstring for Supplier."""

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
