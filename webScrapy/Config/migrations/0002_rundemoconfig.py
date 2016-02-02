# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunDemoConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, verbose_name='\u6a21\u7248\u7279\u5f81URL')),
                ('domains', models.CharField(max_length=255, verbose_name='domains')),
                ('author', models.CharField(max_length=255, verbose_name='\u6a21\u677f\u4f5c\u8005')),
                ('mysql', models.CharField(max_length=255, verbose_name='SQL\u5730\u5740')),
                ('prot', models.CharField(max_length=255, verbose_name='\u7aef\u53e3\u53f7')),
                ('username', models.CharField(max_length=255, verbose_name='\u7528\u6237\u540d')),
                ('passwd', models.CharField(max_length=255, verbose_name='\u5bc6\u7801')),
                ('database', models.CharField(max_length=255, verbose_name='\u5e93\u540d')),
                ('table', models.CharField(max_length=255, verbose_name='\u8868\u660e')),
                ('select_url', models.TextField(default='', verbose_name='\u68c0\u7d22\u6837\u5f0f')),
                ('url_xpath', models.CharField(max_length=255, verbose_name='URL\u68c0\u7d22\u8868\u8fbe\u5f0f')),
                ('url_regex', models.CharField(max_length=255, verbose_name='URL\u6b63\u5219')),
                ('select_title', models.TextField(default='', verbose_name='\u68c0\u7d22\u6837\u5f0f')),
                ('title_xpath', models.CharField(max_length=255, verbose_name='\u6807\u9898\u68c0\u7d22\u8868\u8fbe\u5f0f')),
                ('title_regex', models.CharField(max_length=255, verbose_name='\u6807\u9898\u6b63\u5219')),
                ('select_content', models.TextField(default='', verbose_name='\u68c0\u7d22\u6837\u5f0f')),
                ('content_xpath', models.CharField(max_length=255, verbose_name='\u5185\u5bb9\u68c0\u7d22\u8868\u8fbe\u5f0f')),
                ('content_regex', models.CharField(max_length=255, verbose_name='\u5185\u5bb9\u6b63\u5219')),
                ('select_date', models.TextField(default='', verbose_name='\u68c0\u7d22\u6837\u5f0f')),
                ('date_xpath', models.CharField(max_length=255, verbose_name='\u53d1\u5e03\u65f6\u95f4\u68c0\u7d22\u8868\u8fbe\u5f0f')),
                ('date_regex', models.CharField(max_length=255, verbose_name='\u53d1\u5e03\u65f6\u95f4\u6b63\u5219')),
                ('select_author', models.TextField(default='', verbose_name='\u68c0\u7d22\u6837\u5f0f')),
                ('author_xpath', models.CharField(max_length=255, verbose_name='\u4f5c\u8005\u68c0\u7d22\u8868\u8fbe\u5f0f')),
                ('author_regex', models.CharField(max_length=255, verbose_name='\u4f5c\u8005\u6b63\u5219')),
                ('select_sitename', models.TextField(default='', verbose_name='\u68c0\u7d22\u6837\u5f0f')),
                ('sitename_xpath', models.CharField(max_length=255, verbose_name='\u6765\u6e90\u68c0\u7d22\u8868\u8fbe\u5f0f')),
                ('sitename_regex', models.CharField(max_length=255, verbose_name='\u6765\u6e90\u6b63\u5219')),
                ('select_comment', models.TextField(default='', verbose_name='\u68c0\u7d22\u6837\u5f0f')),
                ('comment_xpath', models.CharField(max_length=255, verbose_name='\u8bc4\u8bba\u68c0\u7d22\u8868\u8fbe\u5f0f')),
                ('comment_regex', models.CharField(max_length=255, verbose_name='\u8bc4\u8bba\u6b63\u5219')),
                ('select_zf', models.TextField(default='', verbose_name='\u68c0\u7d22\u6837\u5f0f')),
                ('zf_xpath', models.CharField(max_length=255, verbose_name='\u8f6c\u53d1\u68c0\u7d22\u8868\u8fbe\u5f0f')),
                ('zf_regex', models.CharField(max_length=255, verbose_name='\u8f6c\u53d1\u6b63\u5219')),
                ('select_ll', models.TextField(default='', verbose_name='\u68c0\u7d22\u6837\u5f0f')),
                ('ll_xpath', models.CharField(max_length=255, verbose_name='\u6d4f\u89c8\u68c0\u7d22\u8868\u8fbe\u5f0f')),
                ('ll_regex', models.CharField(max_length=255, verbose_name='\u6d4f\u89c8\u6b63\u5219')),
            ],
        ),
    ]
