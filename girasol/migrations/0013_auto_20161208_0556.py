# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-08 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('girasol', '0012_auto_20161208_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Autor')),
                ('date', models.DateTimeField(auto_now=True)),
                ('galleries', models.ManyToManyField(blank=True, to='girasol.Gallery')),
                ('links', models.ManyToManyField(blank=True, to='girasol.Post')),
                ('quote', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='girasol.Quote')),
            ],
            options={
                'verbose_name': 'Concepto',
                'verbose_name_plural': 'Conceptos',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ConceptTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='girasol.Concept')),
            ],
            options={
                'verbose_name': 'Concepto Translation',
                'managed': True,
                'default_permissions': (),
                'db_table': 'girasol_concept_translation',
                'db_tablespace': '',
            },
        ),
        migrations.AlterField(
            model_name='quotetranslation',
            name='quote',
            field=models.TextField(verbose_name='Frase'),
        ),
        migrations.AlterUniqueTogether(
            name='concepttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]