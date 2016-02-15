# -*- coding: utf-8 -*-
#! /usr/bin/env python
import scrapy
import MySQLdb
from SpiderConfig.items import PdSpiderItem

def sqlPd():
    conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
    cur  =conn.cursor()
    cur.execute("SELECT title_xpath,title_regex,url_xpath,url_regex,url,domains FROM scrapyproject.config_runpddemo")
    demo =cur.fetchall()[0]
    cur.close()
    conn.close()
    return demo

class PdSpider(scrapy.Spider):
    sql = sqlPd()
    title_xpath = sql[0]
    title_regex = sql[1]
    url_xpath = sql[2]
    url_regex = sql[3]
    url = sql[4]
    domains = sql[5]

    name = 'pd'
    allowed_domains = [domains]
    start_urls = [url]

    def parse(self, response):
        sel = scrapy.Selector(response)
        item = PdSpiderItem()
        item['title'] = sel.xpath(self.title_xpath).extract()
        item['url']   = sel.xpath(self.url_xpath).extract()
        item['url_pd'] = self.url
        yield item
