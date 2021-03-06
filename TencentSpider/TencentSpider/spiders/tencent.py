# -*- coding: utf-8 -*-
import scrapy
#导入链接规则匹配类，用来提取符合规则的链接
from scrapy.linkextractors import LinkExtractor
#导入CrawlSpider类和Rule
from scrapy.spiders import CrawlSpider, Rule
from TencentSpider.items import TencentItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']
    #Response里链接的提取规则，返回符合匹配规则的链接匹配对象的列表
    pagelink = LinkExtractor(allow=("start=\d+"))
    #newlink = LinkExtractor(allow=("1234455"))
    rules = [
        #获取这个列表里的链接，发送请求，并且继续跟进，调用制定的回调函数处理
        Rule(pagelink, callback='parseTencent', follow=True),
        #Rule(newlink, callback='parseTencent', follow=True),
    ]

    def parseTencent(self, response):

        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = TencentItem()
            # 职位名称
            item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            # 详情链接
            item['positionLink'] = each.xpath('./td[1]/a/@href').extract()[0]
            # 职位类别
            item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            # 招聘人数
            item['positionNum'] = each.xpath('./td[3]/text()').extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
            yield item
