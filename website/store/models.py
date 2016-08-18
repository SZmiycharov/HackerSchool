from __future__ import unicode_literals
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=16, blank=True)
    category_logo = models.FileField(blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    maker = models.CharField(max_length=32, blank=True)
    model = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    category = models.ForeignKey(Category)
    product_logo = models.FileField()
    is_in_shopCart = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def __str__(self):
        return self.maker + ' ' + self.model

    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Product, self).save(*args, **kwargs)




