# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from youyuan.items import YouyuanItem

class YySpider(CrawlSpider):
    name = 'yy'
    allowed_domains = ['youyuan.com']
    start_urls = ['http://www.youyuan.com/find/beijing/mm18-25/advance-0-0-0-0-0-0-0/p1/']

    #第一级匹配规则：北京市18-25岁女性的每一页链接匹配规则
    page_links = LinkExtractor(allow=(r"youyuan.com/find/beijing/mm18-25/advance-0-0-0-0-0-0-0/p\d+/"))
    #第二级匹配规则：每个女性个人主页的匹配规则
    profile_links = LinkExtractor(allow=(r"youyuan.com/\d+-profile/"))

    rules = (
        Rule(page_links),
        Rule(profile_links, callback = "parse_item", follow = False),
    )

    def parse_item(self, response):
        item = YouyuanItem()
        item['username'] = self.get_username(response)
        item['age'] = self.get_age(response)
        item['header_url'] = self.get_header_url(response)
        item['image_url'] = self.get_image_url(response)
        item['content'] = self.get_content(response)
        item['place_from'] = self.get_place_from(response)
        item['education'] = self.get_education(response)
        item['hobby'] = self.get_hobby(response)
        item['source_url'] = response.url
        yield item


    def get_username(self,response):
        username = response.xpath('//div')
        if len(username):
            username = username[0]
        else:
            username = "NULL"
        return username.strip()


    def get_age(self,response):
        age = response.xpath('//div')
        if len(age):
            age = re.findall(u"\d+岁",age[0])[0]
        else:
            age = "NULL"
        return age.strip()


    def get_header_url(self,response):
        header_url = response.xpath('//div')
        if len(header_url):
            header_url = header_url[0]
        else:
            header_url = "NULL"
        return header_url.strip()


    def get_image_url(self,response):
        image_url = response.xpath('//div')
        if len(image_url):
            image_url = image_url[0]
        else:
            image_url = "NULL"
        return image_url.strip()


    def get_content(self,response):
        content = response.xpath('//div')
        if len(content):
            content = content[0]
        else:
            content = "NULL"
        return content.strip()



    def get_place_from(self,response):
        place_from = response.xpath('//div')
        if len(place_from):
            place_from = place_from[0]
        else:
            place_from = "NULL"
        return place_from.strip()


    def get_education(self,response):
        education = response.xpath('//div')
        if len(education):
            education = education[0]
        else:
            education = "NULL"
        return education.strip()


    def get_hobby(self,response):
        hobby = response.xpath('//div')
        if len(hobby):
            hobby = ",".join(hobby).replace(" ","")
        else:
            hobby = "NULL"
        return hobby.strip()
