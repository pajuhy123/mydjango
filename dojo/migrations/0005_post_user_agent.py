# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0004_auto_20170813_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_agent',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
