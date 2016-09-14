# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-09-14 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20160914_0945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userproducts',
            options={'verbose_name_plural': 'User'},
        ),
        migrations.AddField(
            model_name='purchases',
            name='priceamount',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='purchases',
            name='pricecurrency',
            field=models.CharField(default='BGN', editable=False, max_length=5, null=True),
        ),
    ]
