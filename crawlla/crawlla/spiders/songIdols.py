# -*- coding: utf-8 -*-
import scrapy
import os

from ..firebase.idols import getIdols
from .. import items


class SongSpider(scrapy.Spider):
    name = "songIdols"
    allowed_domains = [os.environ['targetDomain']]
    start_urls = ('http://' + os.environ['targetDomain'],)

    def parse(self, response):
        # yield scrapy.Request(response.css('#js_oc_box_m1 ul li a::attr("href")').extract_first(), self.parse_topics)
        targets = ['#js_oc_box_m0','#js_oc_box_m1', '#js_oc_box_m2', '#js_oc_box_m3']
        for target in targets:
            for url in response.css(target).css('ul li a::attr("href")').extract():
                yield scrapy.Request(url, self.parse_topics)

    def parse_topics(self, response):
        songIdols = items.SongIdols(
            songName=response.xpath('//*[@id="js_async_main_column_name"]/text()').extract_first().strip(),
            idols= self.parse_idols(response)
        )
        yield songIdols

    def parse_idols(self, response):
        idols = response.xpath('//a[@class="ui_page_match"]/text()').extract()
        idols = [idol.strip() for idol in idols]
        trueIdols = list(getIdols())
        idols = [idol for idol in idols if trueIdols.__contains__(idol)]
        idols = {idol: True for idol in idols}
        return idols
