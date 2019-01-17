# -*- coding: utf-8 -*-
import scrapy


class NuomiSpiderSpider(scrapy.Spider):
    name = 'nuomi_spider'
    allowed_domains = ['nuomi.com']
    start_urls = ['https://www.nuomi.com/changecity']

    def parse(self, response):
        # 获取百度糯米的title
        logo_title = response.xpath("//body//div[@class='logo-area']/a/@title").extract_first()
        print(logo_title)
