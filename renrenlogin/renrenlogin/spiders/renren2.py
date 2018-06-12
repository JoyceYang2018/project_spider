# -*- coding: utf-8 -*-
import scrapy


#正统的模拟登录方法
#首先发送登录页面的get请求，获取到页面登录必须的参数，比如说知乎的_xsrf
#然后和账户密码一起post到服务器，登陆成功
class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    start_urls = (
        'http://www.renren.com/PLogin.do',
    )

    def parse(self, response):
        _xsrf = response.xpath('//_xsrf').extract()[0]
        yield scrapy.FormRequest.from_response(
            response,
            formdata = {"email":"384381523@qq.com","password":"djahhsa","_xsrf":_xsrf},
            callback = self.parse_page
        )


    #def start_requests(self):
    #    for url in self.start_urls:
    #        yield scrapy.FormRequest(url, cookies = self.cookies, callback = self.parse_page)
    def parse_page(self, response):
        print("=======1===" + response.url)
        #with open("deng.html","w") as filename:
        #    filename.write(response.body)
        url = "http://www.renren.com/336189169/profile"
        yield scrapy.Request(url, callback = self.parse_newpage)