# -*- coding: utf-8 -*-
#! /usr/bin/env python
"""webScrapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Config.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,),
    url(r'^pd',pd,name="pd"),
    url(r'^contentpd',contentpd,name="pdcontent"),
    url(r'^demo',demo,),
    url(r'^testpd/$',testpd,),
    url(r'^testcontentpd/$',testcontentpd,),
    url(r'^testdemo/$',testdemo,),
    url(r'^runpd/$',runpd,),
    url(r'^runcontentpd/$',runcontentpd,),
    url(r'^rundemo/$',rundemo,)
]
