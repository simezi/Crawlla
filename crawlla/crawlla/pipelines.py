# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pyrebase
import os

from . import items


class CrawllaPipeline(object):
    def process_item(self, item, spider):
        return item


class FirebaseSongPipeline(object):
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
        if not isinstance(item, items.Song):
           return item

        # self.db.child("songs").set(json.dumps(dict(item), ensure_ascii=False, default=self.process_difficulties))
        self.db.child("songs").child(dict(item)['title']).set(dict(item), json_kwargs={"default": self.process_difficulties})

    def process_difficulties(dif, val):
        if isinstance(val, items.Difficulty):
            return dict(val)
        raise TypeError(repr(val) + " is not JSON serializable")

class FirebaseIdolPipeline(object):
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
        if not isinstance(item, items.Idol):
           return item
        print('idolpipeline')
        self.db.child("idols").child(dict(item)['name']).set(dict(item))