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

@python_2_unicode_compatible
class RunContentPd(models.Model):

    webtype = models.CharField(u'网站类型',max_length=255,null=True,blank=True)
    url  = models.CharField(u'模版特征URL',max_length=255)
    domains  = models.CharField(u'domains',max_length=255)
    author  =   models.CharField(u'模板作者',max_length=255)
    mysql   =   models.CharField(u'SQL地址',max_length=255)
    prot    =   models.CharField('端口号',max_length=255)
    username    =   models.CharField(u'用户名',max_length=255)
    passwd  =   models.CharField(u'密码',max_length=255)
    database    =   models.CharField(u'库名',max_length=255)
    table   =   models.CharField(u'表明',max_length=255)
    select_url  =   models.TextField(u'检索样式',default='')
    url_xpath     =   models.CharField(u'URL检索表达式',max_length=255)
    url_regex     =   models.CharField(u'URL正则',max_length=255)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class RunDemoConfig(models.Model):
    url  = models.CharField(u'模版特征URL',max_length=255)
    domains  = models.CharField(u'domains',max_length=255)
    author  =   models.CharField(u'模板作者',max_length=255)
    mysql   =   models.CharField(u'SQL地址',max_length=255)
    prot    =   models.CharField('端口号',max_length=255)
    username    =   models.CharField(u'用户名',max_length=255)
    passwd  =   models.CharField(u'密码',max_length=255)
    database    =   models.CharField(u'库名',max_length=255)
    table   =   models.CharField(u'表明',max_length=255)
    select_url  =   models.TextField(u'检索样式',default='')
    url_xpath     =   models.CharField(u'URL检索表达式',max_length=255)
    url_regex     =   models.CharField(u'URL正则',max_length=255)
    select_title  =   models.TextField(u'检索样式',default='')
    title_xpath     =   models.CharField(u'标题检索表达式',max_length=255)
    title_regex     =   models.CharField(u'标题正则',max_length=255)
    select_content  =   models.TextField(u'检索样式',default='')
    content_xpath     =   models.CharField(u'内容检索表达式',max_length=255)
    content_regex     =   models.CharField(u'内容正则',max_length=255)
    select_date  =   models.TextField(u'检索样式',default='')
    date_xpath     =   models.CharField(u'发布时间检索表达式',max_length=255)
    date_regex     =   models.CharField(u'发布时间正则',max_length=255)
    select_author  =   models.TextField(u'检索样式',default='')
    author_xpath     =   models.CharField(u'作者检索表达式',max_length=255)
    author_regex     =   models.CharField(u'作者正则',max_length=255)
    select_sitename  =   models.TextField(u'检索样式',default='')
    sitename_xpath     =   models.CharField(u'来源检索表达式',max_length=255)
    sitename_regex     =   models.CharField(u'来源正则',max_length=255)
    select_comment  =   models.TextField(u'检索样式',default='')
    comment_xpath     =   models.CharField(u'评论检索表达式',max_length=255)
    comment_regex     =   models.CharField(u'评论正则',max_length=255)
    select_zf  =   models.TextField(u'检索样式',default='')
    zf_xpath     =   models.CharField(u'转发检索表达式',max_length=255)
    zf_regex     =   models.CharField(u'转发正则',max_length=255)
    select_ll  =   models.TextField(u'检索样式',default='')
    ll_xpath     =   models.CharField(u'浏览检索表达式',max_length=255)
    ll_regex     =   models.CharField(u'浏览正则',max_length=255)

    def __str__(self):
        return self.name