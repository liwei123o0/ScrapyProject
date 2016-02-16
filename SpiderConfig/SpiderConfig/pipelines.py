# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from SpiderConfig.items import PdSpiderItem
import MySQLdb
class SpiderconfigPipeline(object):

    def process_item(self, item, spider):
        return item

class SpiderPdPipeline(object):

    def open_spider(self,spider):
        self.conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",charset="utf8")
        self.cur  =self.conn.cursor()

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()

    def process_item(self,item,spider):
        if item['url'] != list:
            for i in xrange(len(item['url'])):
                try :
                    self.cur.execute("INSERT INTO scrapyproject.spider_pd (url,title,url_pd) VALUES ('%s','%s','%s')"%(item['url'][i],item['title'][i],item['url_pd']))
                except MySQLdb.Error,e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                    continue
                self.conn.commit()
        else:
            self.cur.execute("INSERT INTO scrapyproject.spider_pd (url,title,url_pd) VALUES ('%s','%s','%s')"%(item['url'],item['title'],item['url_pd']))
            self.conn.commit()
        return item