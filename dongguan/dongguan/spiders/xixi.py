# -*- coding: utf-8 -*-
import scrapy
from dongguan.items import DongguanItem

class SunSpider(scrapy.Spider):
    name = 'xixi'
    allowed_domains = ['wz.sun0769.com']
    urls = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [urls + str(offset)]




    def parse(self,response):
        #每一页所有帖子链接集合
        links = response.xpath('//div[@class="greyframe"]/table//td/a[@class="news14"]/@href').extract()
        for link in links:
            #提取列表里每个帖子的链接，发送请求并调用parse_item来处理
            yield scrapy.Request(link,callback=self.parse_item)
        #页面终止条件成立前，会一直自增offse的值，并发送新的页面请求，调用parse方法处理
        if self.offset <= 90120:
            self.offset += 30
            #发送请求，调用self.parse
            yield scrapy.Request(self.urls + str(self.offset), callback = self.parse)


    def parse_item(self, response):
        #print response.url
        
        item = DongguanItem()
        item['title'] = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        item['number'] = item['title'].split(' ')[-1].split(':')[-1]
        #先取有图片的内容，如果有内容，返回所有列表内容的列表集合；如果没有图片，则这个列表为空
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        #再使用以下匹配规则
        if len(content)==0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()
        item['url'] = response.url
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        yield item
 



