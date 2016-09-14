from __future__ import unicode_literals
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
import django
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
import sys


def f():
    d = uuid.uuid4()
    str = d.hex
    return str[0:16]


class Category(models.Model):
    allowed_user = models.ManyToManyField(User)
    name = models.CharField(max_length=16, blank=True, db_index=True, unique=True)
    id = models.CharField(max_length=100, primary_key=True, default=f)
    category_logo = ProcessedImageField(upload_to='images', processors=[ResizeToFill(960, 540)], format='JPEG')
    category_logo_thumbnail = ImageSpecField(source='category_logo', format='JPEG', processors=[ResizeToFill(240, 135)])
    created = models.DateTimeField(editable=False, default=django.utils.timezone.now, db_index=True)
    modified = models.DateTimeField(editable=False, default=django.utils.timezone.now)

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_logo = ProcessedImageField(upload_to='images', processors=[ResizeToFill(960, 540)], format='JPEG')
    product_logo_thumbnail = ImageSpecField(source='product_logo', format='JPEG', processors=[ResizeToFill(240, 135)])
    created = models.DateTimeField(editable=False, db_index=True)
    modified = models.DateTimeField(editable=False)
    quantity = models.PositiveIntegerField(default=1)

    def currency(self):
        return str(self.price).split(' ')[1]

    def moneyamount(self):
        return float(str(self.price).split(' ')[0])

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


class Purchases(models.Model):
    user = models.ForeignKey(User, editable=False, default=1)
    made_at = models.DateTimeField(editable=False, default=django.utils.timezone.now)
    quantity = models.IntegerField(default=1, null=True)
    product = models.ForeignKey(Product)
    address = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=15)
    delivered = models.BooleanField(default=False)
    totalprice = MoneyField(max_digits=10, decimal_places=2, default_currency='BGN', editable=False)
    priceamount = models.DecimalField(max_digits=10, decimal_places=2, editable=False, null=True)
    pricecurrency = models.CharField(max_length=5, default='BGN', editable=False, null=True)

    priceamount.lookup_range = (
        (None, ('All')),
        ([0, 100], '0-100'),
        ([100, 200], '100-200'),
        ([200, 300], '200-300'),
        ([300, 500], '300-500'),
        ([500, None], '500+'),
    )

    def subject_totalprice(self):
        print >> sys.stderr, "quantity: {}".format(self.quantity)
        return self.quantity * Product.objects.filter(id=self.product.id)[0].moneyamount()

    def subject_priceamount(self):
        return str(self.totalprice).split(' ')[0]

    def subject_pricecurrency(self):
        return str(self.totalprice).split(' ')[1]

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'Purchases'

    def save(self, *args, **kwargs):
        if not self.id:
            self.totalprice = self.subject_totalprice()
            self.priceamount = self.subject_priceamount()
            self.pricecurrency = self.subject_pricecurrency()
        return super(Purchases, self).save(*args, **kwargs)


class UserProducts(models.Model):
    user = models.ForeignKey(User, editable=False, default=1)
    added_at = models.DateTimeField(editable=False, default=django.utils.timezone.now)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1, null=True)
    in_shop_cart = models.BooleanField(default=False)
    totalprice = MoneyField(max_digits=10, decimal_places=2, default_currency='BGN', editable=False)

    def subject_totalprice(self):
        print >> sys.stderr, "quantity: {}".format(self.quantity)
        return self.quantity * Product.objects.filter(id=self.product.id)[0].moneyamount()

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'User'

    def save(self, *args, **kwargs):
        if not self.id:
            self.totalprice = self.subject_totalprice()
        return super(UserProducts, self).save(*args, **kwargs)

























