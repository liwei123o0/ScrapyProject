# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Config', '0002_rundemoconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rundemoconfig',
            name='content_regex',
            field=models.CharField(max_length=255, verbose_name='\u6b63\u5219'),
        ),
        migrations.AlterField(
            model_name='rundemoconfig',
            name='content_xpath',
            field=models.CharField(max_length=255, verbose_name='\u68c0\u7d22\u8868\u8fbe\u5f0f'),
        ),
    ]