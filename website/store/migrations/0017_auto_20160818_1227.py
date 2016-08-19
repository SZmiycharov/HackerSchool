# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-18 12:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20160818_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 12, 27, 9, 129990, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 12, 27, 9, 130046, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 12, 27, 9, 142170, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(default=store.models.f, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 18, 12, 27, 9, 142224, tzinfo=utc), editable=False),
        ),
    ]