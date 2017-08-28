# -*- coding: utf-8 -*-
import scrapy
import os

from .. import items


class SongSpider(scrapy.Spider):
    name = "song"
    allowed_domains = [os.environ['targetDomain']]
    start_urls = ('http://' + os.environ['targetDomain'],)

    def parse(self, response):
        # yield scrapy.Request(response.css('#js_oc_box_m1 ul li a::attr("href")').extract_first(), self.parse_topics)
        targets = ['#js_oc_box_m0','#js_oc_box_m1', '#js_oc_box_m2', '#js_oc_box_m3']
        for target in targets:
            for url in response.css(target).css('ul li a::attr("href")').extract():
                yield scrapy.Request(url, self.parse_topics)

    def parse_topics(self, response):
        typeOrg = response.xpath('//*[@id="js_async_main_column_text"]/div[1]/table[1]/tbody/tr/td[3]/span')
        if len(typeOrg.xpath('a')) > 0 :
            typeOrg = typeOrg.xpath('a/text()')
        else:
            typeOrg = typeOrg.xpath('text()')
        song = items.Song(
            title=response.xpath('//*[@id="js_async_main_column_name"]/text()').extract_first().strip(),
            bpm=response.xpath(
                '//*[@id="js_async_main_column_text"]/div[1]/table[1]/tbody/tr/td[1]/span/text()').extract_first(),
            time=response.xpath(
                '//*[@id="js_async_main_column_text"]/div[1]/table[1]/tbody/tr/td[2]/span/text()').extract_first(),
            type=typeOrg.extract_first(),
            category=response.xpath(
                '//*[@id="js_async_main_column_text"]/div[1]/table[1]/tbody/tr/td[4]/span/text()').extract_first(),
            start=response.xpath(
                '//*[@id="js_async_main_column_text"]/div[1]/table[1]/tbody/tr/td[5]/span/text()').extract_first(),
            difficulties=list(self.parse_difficulties(response))
        )

        yield song

    def parse_difficulties(self, response):
        difficulties = response.xpath('//*[@id="js_async_main_column_text"]/div[1]/table[2]/tbody/tr')
        for difficulty in difficulties:
            yield items.Difficulty(
                rank=difficulty.xpath("th[1]/span/text()").extract_first(),
                level=difficulty.xpath("td[2]/span/text()").extract_first(),
                stamina=difficulty.xpath("td[3]/span/text()").extract_first(),
                notes=difficulty.xpath("td[4]/span/text()").extract_first(),
                density=difficulty.xpath("td[5]/span/text()").extract_first(),
            )
