# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 23:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.Customer'),
        ),
    ]