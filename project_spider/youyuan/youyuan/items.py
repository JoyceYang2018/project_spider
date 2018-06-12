# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item
import scrapy


class YouyuanItem(scrapy.Item):
    username = Field()
    age = Field()
    #头像图片链接
    header_url = Field()
    #相册图片链接
    image_url = Field()
    #内心独白
    content = Field()
    place_from = Field()
    education = Field()
    hobby = Field()
    #个人主页
    source_url = Field()

