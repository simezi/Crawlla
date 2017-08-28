# -*- coding: utf-8 -*-
import scrapy
import os

from .. import items


class IdolSpider(scrapy.Spider):
    name = "idol"
    allowed_domains = [os.environ['targetDomain']]
    start_urls = ('http://' + os.environ['targetDomain'],)

    def parse(self, response):
        # yield scrapy.Request(response.css('#js_oc_box_m4 ul li ul li a::attr("href")').extract_first(), self.parse_idol)
        targets = ['#js_oc_box_m4','#js_oc_box_m5', '#js_oc_box_m6']
        for target in targets:
            for url in response.css(target).css('ul li ul li a::attr("href")').extract():
                yield scrapy.Request(url, self.parse_idol)

    def parse_idol(self, response):
        idol = items.Idol()

        idol['name'] = response.xpath('//*[@id="js_async_main_column_name"]/text()').extract_first().strip()
        idol['nameHiragana'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[2]/td[2]/text()').extract_first()
        idol['type'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[3]/td/a/text()').extract_first()
        idol['birthday'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[4]/td/text()').extract_first()
        idol['constellation'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[5]/td/text()').extract_first()
        idol['bloodType'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[6]/td/text()').extract_first()

        idol['height'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[7]/td/text()').extract_first()
        idol['weight'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[7]/td/text()').extract_first()

        idol['bust'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[8]/td/text()').extract_first()
        idol['waist'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[8]/td/text()').extract_first()
        idol['hip'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[8]/td/text()').extract_first()

        idol['hand'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[9]/td/text()').extract_first()
        idol['birth'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[10]/td/text()').extract_first()
        idol['cv'] = response.xpath('//*[@id="js_async_main_column_text"]/table[1]/tbody/tr[11]/td/a/text()').extract_first()
        print(idol)
        yield idol