# -*- coding: utf-8 -*-
#! /usr/bin/env python
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class PdlistURL(models.Model):

    name = models.CharField(u'网站名',max_length=255)
    url  = models.CharField(u'URL',max_length=255)
    domains  = models.CharField(u'domains',max_length=255)
    author  =   models.CharField(u'模板作者',max_length=255)
    title_xpath   =   models.CharField(u'标题检索表达式',max_length=255)
    title_regex   =   models.CharField(u'标题正则',max_length=255)
    url_xpath     =   models.CharField(u'URL检索表达式',max_length=255)
    url_regex     =   models.CharField(u'URL正则',max_length=255)

    def __str__(self):
        return self.name