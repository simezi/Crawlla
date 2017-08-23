# -*- coding: utf-8 -*-
import scrapy

from .. import items


class SongSpider(scrapy.Spider):
    name = "song"
    allowed_domains = ["imascg-slstage-wiki.gamerch.com"]
    start_urls = ('http://imascg-slstage-wiki.gamerch.com/',)

    def parse(self, response):
        # yield scrapy.Request(response.css('#js_oc_box_m0 ul li a::attr("href")').extract_first(), self.parse_topics)
         for url in response.css('#js_oc_box_m0 ul li a::attr("href")').extract():
             yield scrapy.Request(url, self.parse_topics)

    def parse_topics(self, response):
        song = items.Song(
            title=response.xpath('//*[@id="js_async_main_column_name"]/text()').extract_first().strip(),
            bpm=response.xpath(
                '//*[@id="js_async_main_column_text"]/div[1]/table/tbody/tr/td[1]/span/text()').extract_first(),
            time=response.xpath(
                '//*[@id="js_async_main_column_text"]/div[1]/table/tbody/tr/td[2]/span/text()').extract_first(),
            type=response.xpath(
                '//*[@id="js_async_main_column_text"]/div[1]/table/tbody/tr/td[3]/span/text()').extract_first(),
            category=response.xpath(
                '//*[@id="js_async_main_column_text"]/div[1]/table/tbody/tr/td[4]/span/text()').extract_first(),
            start=response.xpath(
                '//*[@id="js_async_main_column_text"]/div[1]/table/tbody/tr/td[5]/span/text()').extract_first(),
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
