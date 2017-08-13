# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 05:31
from __future__ import unicode_literals

from django.db import migrations, models
import dojo.models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[dojo.models.min_length_3_validator]),
        ),
    ]