# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 07:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaApp', '0005_remove_image_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photos',
        ),
    ]
