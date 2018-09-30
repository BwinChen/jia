# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Field, Item


class ImageItem(Item):
    table = 'jiacomimages'
    page_url = Field()
    img_src = Field()
    crawled_at = Field()
