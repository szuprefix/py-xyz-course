# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-06-15 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='\u540d\u79f0'),
        ),
    ]
