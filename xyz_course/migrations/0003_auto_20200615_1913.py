# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-06-15 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20200615_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='\u7b80\u4ecb'),
        ),
        migrations.AddField(
            model_name='course',
            name='outline',
            field=models.TextField(blank=True, default='', verbose_name='\u5927\u7eb2'),
        ),
    ]
