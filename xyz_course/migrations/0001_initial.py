# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-01-23 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import xyz_util.modelutils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='\u540d\u79f0')),
                ('code', models.CharField(blank=True, db_index=True, default='', max_length=64, verbose_name='\u62fc\u97f3\u7f29\u5199')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7c7b\u522b',
                'verbose_name_plural': '\u7c7b\u522b',
            },
            bases=(xyz_util.modelutils.CodeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u540d\u79f0')),
                ('code', models.CharField(blank=True, db_index=True, default='', max_length=64, verbose_name='\u62fc\u97f3\u7f29\u5199')),
                ('order_num', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='\u5e8f\u53f7')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7ae0\u8282',
                'verbose_name_plural': '\u7ae0\u8282',
            },
            bases=(xyz_util.modelutils.CodeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='\u540d\u79f0')),
                ('code', models.CharField(blank=True, db_index=True, default='', max_length=64, verbose_name='\u62fc\u97f3\u7f29\u5199')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u6709\u6548')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='course.Category', verbose_name='\u7c7b\u522b')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
            bases=(xyz_util.modelutils.CodeMixin, models.Model),
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chapters', to='course.Course', verbose_name='\u8bfe\u7a0b'),
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set([('course', 'name')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='chapter',
            order_with_respect_to='course',
        ),
    ]
