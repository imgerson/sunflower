# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-15 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('girasol', '0015_auto_20161209_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concept',
            name='links',
        ),
        migrations.RemoveField(
            model_name='post',
            name='links',
        ),
    ]