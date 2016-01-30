# -*- coding: utf-8 -*-
#! /usr/bin/env python
from django.shortcuts import render
from .models import *


def index(request):
    return render(request,'index.html')

def pd(request):
    return  render(request,'pd.html')

def nr(request):
    return render(request, 'nr.html')

def listpd(request):

    name = str(request.POST['name'])
    url  = str(request.POST['url'])
    domains = str(request.POST['domains'])
    author  = str(request.POST['author'])
    mysql   = str(request.POST['mysql'])
    prot    = str(request.POST['prot'])
    username  = str(request.POST['username'])
    passwd    = str(request.POST['passwd'])
    database = str(request.POST['database'])
    table   =   str(request.POST['table'])
    # xpath_title = str(request.POST['xpath_title'])
    # css_title   =   str(request.POST['css_title'])
    # select_title  = str(request.POST['select_title'])
    title_xpath =   str(request.POST['title_xpath'])
    title_regex =   str(request.POST['title_regex'])
    # title_test  =   str(request.POST['title_test'])
    # select_url  = str(request.POST['select_url'])
    url_xpath   =   str(request.POST['url_xpath'])
    url_regex   =   str(request.POST['url_regex'])
    # url_test    =   str(request.POST['url_test'])

    return  render(request,'pd.html',{"name":name,
                                      'url':url,
                                      'domains':domains,
                                      'author':author,
                                      'mysql':mysql,
                                      'prot':prot,
                                      'username':username,
                                      'passwd':passwd,
                                      'database':database,
                                      'table':table,
                                      # 'select_title':select_title,
                                      # 'xpath_title':xpath_title,
                                      # 'css_title':css_title,
                                      'title_xpath':title_xpath,
                                      'title_regex':title_regex,
                                      # 'title_test':title_test,
                                      # 'select_url':select_url,
                                      'url_xpath':url_xpath,
                                      'url_regex':url_regex,
                                      # 'url_test':url_test,
                                      })
