#coding=utf-8
from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    #启动所有slaver端爬虫的指令，下面的格式市参考格式，建议采用这种格式
    redis_key = 'myspider:start_urls'

    #指定爬取域范围
    #allowed_domains = ["dmoz.org"]

    #动态获取爬取域范围
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        #调用父类初始化方法
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
