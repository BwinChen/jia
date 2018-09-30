# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from jia.items import ImageItem


class JiacomSpider(Spider):
    name = 'jiacom'
    allowed_domains = ['jia.com']
    # start_urls = ['http://www.jia.com/']
    start_url = 'http://www.jia.com/xiamen/'

    def start_requests(self):
        yield Request(self.start_url, callback=self.parse)

    def parse(self, response):
        # 解析图片
        srcs = response.xpath('//img/@src').extract()
        # j_region = response.css('#J_region::text').extract_first()
        for src in srcs:
            src = response.urljoin(src)
            # self.logger.debug('src:' + src)
            image_item = ImageItem()
            image_item['page_url'] = response.url
            image_item['img_src'] = src
            yield image_item
        # 生成新请求
        hrefs = response.xpath('//a/@href').extract()
        for href in hrefs:
            href = response.urljoin(href)
            if 'javascript' not in href and 'tuku' not in href and 'luntan' not in href:
                # self.logger.debug('href:' + href)
                yield Request(href, callback=self.parse)
