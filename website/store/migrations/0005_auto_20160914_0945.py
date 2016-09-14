# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-09-14 06:45
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_auto_20160913_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('quantity', models.IntegerField(default=1, null=True)),
                ('in_shop_cart', models.BooleanField(default=False)),
                ('totalprice_currency', djmoney.models.fields.CurrencyField(choices=[(b'BGN', 'Bulgarian Lev'), (b'EUR', 'Euro'), (b'USD', 'US Dollar')], default='BGN', editable=False, max_length=3)),
                ('totalprice', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency=b'BGN', editable=False, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'UserProducts',
                'indexes': [],
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(db_index=True, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='totalprice',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency=b'BGN', editable=False, max_digits=10),
        ),
        migrations.AddField(
            model_name='userproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
        migrations.AddField(
            model_name='userproducts',
            name='user',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
