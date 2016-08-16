from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=16, blank=True)
    category_logo = models.FileField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    maker = models.CharField(max_length=32, blank=True)
    model = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    category = models.ForeignKey(Category)
    product_logo = models.FileField(blank=True)
    is_in_shopCart = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.maker + ' ' + self.model

