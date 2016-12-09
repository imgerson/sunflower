# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-22 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girasol', '0004_gallery_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='posts',
            field=models.ManyToManyField(blank=True, to='girasol.Post'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='galleries',
            field=models.ManyToManyField(blank=True, to='girasol.Gallery'),
        ),
    ]