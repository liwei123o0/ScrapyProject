# -*- coding: utf-8 -*-
#! /usr/bin/env python
from django.shortcuts import render
from .models import RunPdDemo,RunContentPd,RunDemoConfig

def index(request):
    return render(request,'index.html')

def pd(request):
    return  render(request,'pd.html')

def contentpd(request):
    return render(request,'contentpd.html')

def demo(request):
    return render(request,'content.html')

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

def testdemo(request):

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
    select_title  = request.POST['select_title']
    title_xpath   =   request.POST['title_xpath']
    title_regex   =   request.POST['title_regex']
    select_content  = request.POST['select_content']
    content_xpath   =   request.POST['content_xpath']
    content_regex   =   request.POST['content_regex']
    select_date  = request.POST['select_date']
    date_xpath   =   request.POST['date_xpath']
    date_regex   =   request.POST['date_regex']
    select_author  = request.POST['select_author']
    author_xpath   =   request.POST['author_xpath']
    author_regex   =   request.POST['author_regex']
    select_sitename  = request.POST['select_sitename']
    sitename_xpath   =   request.POST['sitename_xpath']
    sitename_regex   =   request.POST['sitename_regex']
    select_comment  = request.POST['select_comment']
    comment_xpath   =   request.POST['comment_xpath']
    comment_regex   =   request.POST['comment_regex']
    select_zf  = request.POST['select_zf']
    zf_xpath   =   request.POST['zf_xpath']
    zf_regex   =   request.POST['zf_regex']
    select_ll  = request.POST['select_ll']
    ll_xpath   =   request.POST['ll_xpath']
    ll_regex   =   request.POST['ll_regex']

    return  render(request,'content.html',{
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
                                    'select_title':select_title,
                                    'title_xpath':title_xpath,
                                    'title_regex':title_regex,
                                    'select_content':select_content,
                                    'content_xpath':content_xpath,
                                    'content_regex':content_regex,
                                    'select_date':select_date,
                                    'date_xpath':date_xpath,
                                    'date_regex':date_regex,
                                    'select_author':select_author,
                                    'author_xpath':author_xpath,
                                    'author_regex':author_regex,
                                    'select_sitename':select_sitename,
                                    'sitename_xpath':sitename_xpath,
                                    'sitename_regex':sitename_regex,
                                    'select_comment':select_comment,
                                    'comment_xpath':comment_xpath,
                                    'comment_regex':comment_regex,
                                    'select_zf':select_zf,
                                    'zf_xpath':zf_xpath,
                                    'zf_regex':zf_regex,
                                    'select_ll':select_ll,
                                    'll_xpath':ll_xpath,
                                    'll_regex':ll_regex,
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

def rundemo(request):

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
    select_title  = request.POST['select_title']
    title_xpath   =   request.POST['title_xpath']
    title_regex   =   request.POST['title_regex']
    select_content  = request.POST['select_content']
    content_xpath   =   request.POST['content_xpath']
    content_regex   =   request.POST['content_regex']
    select_date  = request.POST['select_date']
    date_xpath   =   request.POST['date_xpath']
    date_regex   =   request.POST['date_regex']
    select_author  = request.POST['select_author']
    author_xpath   =   request.POST['author_xpath']
    author_regex   =   request.POST['author_regex']
    select_sitename  = request.POST['select_sitename']
    sitename_xpath   =   request.POST['sitename_xpath']
    sitename_regex   =   request.POST['sitename_regex']
    select_comment  = request.POST['select_comment']
    comment_xpath   =   request.POST['comment_xpath']
    comment_regex   =   request.POST['comment_regex']
    select_zf  = request.POST['select_zf']
    zf_xpath   =   request.POST['zf_xpath']
    zf_regex   =   request.POST['zf_regex']
    select_ll  = request.POST['select_ll']
    ll_xpath   =   request.POST['ll_xpath']
    ll_regex   =   request.POST['ll_regex']

    RunDemoConfig.objects.create(url=url,
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
                             url_regex=url_regex,
                            select_title=select_title,
                            title_xpath=title_xpath,
                            title_regex=title_regex,
                            select_content=select_content,
                            content_xpath=content_xpath,
                            content_regex=content_regex,
                            select_date=select_date,
                            date_xpath=date_xpath,
                            date_regex=date_regex,
                            select_author=select_author,
                            author_xpath=author_xpath,
                            author_regex=author_regex,
                            select_sitename=select_sitename,
                            sitename_xpath=sitename_xpath,
                            sitename_regex=sitename_regex,
                            select_comment=select_comment,
                            comment_xpath=comment_xpath,
                            comment_regex=comment_regex,
                            select_zf=select_zf,
                            zf_xpath=zf_xpath,
                            zf_regex=zf_regex,
                            select_ll=select_ll,
                            ll_xpath=ll_xpath,
                            ll_regex=ll_regex,
    )
    return render(request,'success.html')