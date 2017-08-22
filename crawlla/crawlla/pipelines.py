# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pyrebase
import os


class CrawllaPipeline(object):
    def process_item(self, item, spider):
        return item


class FirebasePipeline(object):
    def open_spider(self, spider):
        config = {
            "apiKey": os.environ['apiKey'],
            "authDomain": os.environ['authDomain'],
            "databaseURL": os.environ['databaseURL'],
            "storageBucket": os.environ['storageBucket'],
            "serviceAccount": os.environ['serviceAccount']
        }
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def process_item(self, item, spider):
        self.db.child("songs").set(json.dumps(dict(item),ensure_ascii=False))