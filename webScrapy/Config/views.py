# -*- coding: utf-8 -*-
#! /usr/bin/env python
from django.shortcuts import render
from .models import RunPdDemo,RunContentPd

def index(request):
    return render(request,'index.html')

def pd(request):
    return  render(request,'pd.html')

def contentpd(request):
    return render(request,'contentpd.html')

def nr(request):
    return render(request, 'nr.html')

def testpd(request):

    name = request.POST['name']
    url  = request.POST['url']
    domains = request.POST['domains']
    author  = request.POST['author']
    mysql   = request.POST['mysql']
    prot    = request.POST['prot']
    username  = request.POST['username']
    passwd    = request.POST['passwd']
    database = request.POST['database']
    table   =   request.POST['table']
    select_title  = request.POST['select_title']
    title_xpath =   request.POST['title_xpath']
    title_regex =   request.POST['title_regex']
    select_url  = request.POST['select_url']
    url_xpath   =   request.POST['url_xpath']
    url_regex   =   request.POST['url_regex']

    if name =="":
        return  render(request,'NotNull.html')
    if url =="":
        return  render(request,'NotNull.html')
    if domains =="":
        return  render(request,'NotNull.html')
    if author =="":
        return  render(request,'NotNull.html')
    if mysql =="":
        return  render(request,'NotNull.html')
    if prot =="":
        return  render(request,'NotNull.html')
    if username =="":
        return  render(request,'NotNull.html')
    if passwd =="":
        return  render(request,'NotNull.html')
    if database =="":
        return  render(request,'NotNull.html')
    if table =="":
        return  render(request,'NotNull.html')
    if title_xpath =="":
        return  render(request,'NotNull.html')
    if url_xpath =="":
        return  render(request,'NotNull.html')

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
                                      'select_title':select_title,
                                      'title_xpath':title_xpath,
                                      'title_regex':title_regex,
                                      'select_url':select_url,
                                      'url_xpath':url_xpath,
                                      'url_regex':url_regex,
                                      })
def testcontentpd(request):

    webtype = request.POST['webtype']
    print webtype
    url  = request.POST['url']
    domains = request.POST['domains']
    author  = request.POST['author']
    mysql   = request.POST['mysql']
    prot    = request.POST['prot']
    username  = request.POST['username']
    passwd    = request.POST['passwd']
    database = request.POST['database']
    table   =   request.POST['table']
    select_url  = request.POST['select_url']
    url_xpath   =   request.POST['url_xpath']
    url_regex   =   request.POST['url_regex']

    if webtype =="":
        return  render(request,'NotNull.html')
    if url =="":
        return  render(request,'NotNull.html')
    if domains =="":
        return  render(request,'NotNull.html')
    if author =="":
        return  render(request,'NotNull.html')
    if mysql =="":
        return  render(request,'NotNull.html')
    if prot =="":
        return  render(request,'NotNull.html')
    if username =="":
        return  render(request,'NotNull.html')
    if passwd =="":
        return  render(request,'NotNull.html')
    if database =="":
        return  render(request,'NotNull.html')
    if table =="":
        return  render(request,'NotNull.html')
    if url_xpath =="":
        return  render(request,'NotNull.html')

    return  render(request,'contentpd.html',{
                                    'webtype':webtype,
                                    'url':url,
                                    'domains':domains,
                                    'author':author,
                                    'mysql':mysql,
                                    'prot':prot,
                                    'username':username,
                                    'passwd':passwd,
                                    'database':database,
                                    'table':table,
                                    'select_url':select_url,
                                    'url_xpath':url_xpath,
                                    'url_regex':url_regex,
                                      })

def runpd(request):

    name = request.POST['name']
    url  = request.POST['url']
    domains = request.POST['domains']
    author  = request.POST['author']
    mysql   = request.POST['mysql']
    prot    = request.POST['prot']
    username  = request.POST['username']
    passwd    = request.POST['passwd']
    database = request.POST['database']
    table   =   request.POST['table']
    select_title  = request.POST['select_title']
    title_xpath =   request.POST['title_xpath']
    title_regex =   request.POST['title_regex']
    select_url  = request.POST['select_url']
    url_xpath   =   request.POST['url_xpath']
    url_regex   =   request.POST['url_regex']

    if name =="":
        return  render(request,'NotNull.html')
    if url =="":
        return  render(request,'NotNull.html')
    if domains =="":
        return  render(request,'NotNull.html')
    if author =="":
        return  render(request,'NotNull.html')
    if mysql =="":
        return  render(request,'NotNull.html')
    if prot =="":
        return  render(request,'NotNull.html')
    if username =="":
        return  render(request,'NotNull.html')
    if passwd =="":
        return  render(request,'NotNull.html')
    if database =="":
        return  render(request,'NotNull.html')
    if table =="":
        return  render(request,'NotNull.html')
    if title_xpath =="":
        return  render(request,'NotNull.html')
    if url_xpath =="":
        return  render(request,'NotNull.html')

    RunPdDemo.objects.create(name=name,
                         url=url,
                         domains=domains,
                         author=author,
                         mysql=mysql,
                         prot=prot,
                         username=username,
                         passwd=passwd,
                         database=database,
                         table=table,
                         select_title=select_title,
                         title_xpath=title_xpath,
                         title_regex=title_regex,
                         select_url=select_url,
                         url_xpath=url_xpath,
                         url_regex=url_regex)

    return render(request,'success.html')

def runcontentpd(request):

    webtype = request.POST['webtype']
    print webtype
    url  = request.POST['url']
    domains = request.POST['domains']
    author  = request.POST['author']
    mysql   = request.POST['mysql']
    prot    = request.POST['prot']
    username  = request.POST['username']
    passwd    = request.POST['passwd']
    database = request.POST['database']
    table   =   request.POST['table']
    select_url  = request.POST['select_url']
    url_xpath   =   request.POST['url_xpath']
    url_regex   =   request.POST['url_regex']

    if webtype =="":
        return  render(request,'NotNull.html')
    if url =="":
        return  render(request,'NotNull.html')
    if domains =="":
        return  render(request,'NotNull.html')
    if author =="":
        return  render(request,'NotNull.html')
    if mysql =="":
        return  render(request,'NotNull.html')
    if prot =="":
        return  render(request,'NotNull.html')
    if username =="":
        return  render(request,'NotNull.html')
    if passwd =="":
        return  render(request,'NotNull.html')
    if database =="":
        return  render(request,'NotNull.html')
    if table =="":
        return  render(request,'NotNull.html')
    if url_xpath =="":
        return  render(request,'NotNull.html')

    RunContentPd.objects.create(webtype=webtype,
                         url=url,
                         domains=domains,
                         author=author,
                         mysql=mysql,
                         prot=prot,
                         username=username,
                         passwd=passwd,
                         database=database,
                         table=table,
                         select_url=select_url,
                         url_xpath=url_xpath,
                         url_regex=url_regex,)
    return render(request,'success.html')