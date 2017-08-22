# -*- coding: utf-8 -*-
import scrapy

from .. import items


class WikiSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["imascg-slstage-wiki.gamerch.com"]
    start_urls = ('http://imascg-slstage-wiki.gamerch.com/',)

    def parse(self, response):
        # yield scrapy.Request(response.css('#js_oc_box_m0 ul li a::attr("href")').extract_first(),self.parse_topics)
        for url in response.css('#js_oc_box_m0 ul li a::attr("href")').extract():
            yield scrapy.Request(url, self.parse_topics)

    def parse_topics(self, response):
        item = items.Song()
        item['title'] = response.xpath('//*[@id="js_async_main_column_name"]/text()').extract_first().strip()
        print(item['title'])
        yield item
