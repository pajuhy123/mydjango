# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='blog/post'),
        ),
    ]
