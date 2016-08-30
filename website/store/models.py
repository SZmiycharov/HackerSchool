from __future__ import unicode_literals
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField


def f():
    d = uuid.uuid4()
    str = d.hex
    return str[0:16]


class Category(models.Model):
    allowed_user = models.ManyToManyField(User)
    name = models.CharField(max_length=16, blank=True, db_index=True, unique=True)
    id = models.CharField(max_length=100, primary_key=True, default=f)
    category_logo = models.ImageField(blank=True, upload_to='images')
    category_logo_thumbnail = ImageSpecField(source='category_logo', format='JPEG', options={'quality': 60})
    created = models.DateTimeField(editable=False, default=timezone.now(), db_index=True)
    modified = models.DateTimeField(editable=False, default=timezone.now())

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
    maker = models.CharField(max_length=32, blank=True, db_index=True)
    model = models.CharField(max_length=32, blank=True, db_index=True)
    id = models.CharField(max_length=100, primary_key=True, default=f)
    description = models.TextField(blank=True)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='BGN')
    category = models.ForeignKey(Category)
    product_logo = models.ImageField(blank=True)
    product_logo_thumbnail = ImageSpecField(source='product_logo', format='JPEG', options={'quality': 60})
    is_in_shopCart = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(editable=False, default=timezone.now(), db_index=True)
    modified = models.DateTimeField(editable=False, default=timezone.now())
    quantity = models.IntegerField(default=1)


    def currency(self):
        return str(self.price).split(' ')[1]

    def __str__(self):
        return self.maker + ' ' + self.model

    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Product, self).save(*args, **kwargs)


    class Meta:
        unique_together = ('maker', 'model',)




