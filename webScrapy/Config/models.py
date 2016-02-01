# -*- coding: utf-8 -*-
#! /usr/bin/env python
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class RunPdDemo(models.Model):

    name = models.CharField(u'网站名',max_length=255,null=True,blank=True)
    url  = models.CharField(u'URL',max_length=255)
    domains  = models.CharField(u'domains',max_length=255)
    author  =   models.CharField(u'模板作者',max_length=255)
    mysql   =   models.CharField(u'SQL地址',max_length=255)
    prot    =   models.CharField('端口号',max_length=255)
    username    =   models.CharField(u'用户名',max_length=255)
    passwd  =   models.CharField(u'密码',max_length=255)
    database    =   models.CharField(u'库名',max_length=255)
    table   =   models.CharField(u'表明',max_length=255)
    select_title    =   models.TextField(u'检索样式',default='')
    title_xpath   =   models.CharField(u'标题检索表达式',max_length=255)
    title_regex   =   models.CharField(u'标题正则',max_length=255)
    select_url  =   models.TextField(u'检索样式',default='')
    url_xpath     =   models.CharField(u'URL检索表达式',max_length=255)
    url_regex     =   models.CharField(u'URL正则',max_length=255)

    def __str__(self):
        return self.name