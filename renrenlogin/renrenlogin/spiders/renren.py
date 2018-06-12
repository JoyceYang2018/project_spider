# -*- coding: utf-8 -*-
import scrapy

#实在没办法了，可以用这种方法模拟登录，成功率100%

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = (
        'http://www.renren.com/xxxx',
        'http://www.renren.com/1111',
        'http://www.renren.com/xx',
    )

    #太懒，不改了
    cookies = {
    "anonymid" : "jgsstk4hrvnt1c",
    "depovince" : "HUB",
    "_r01_" : "1",
    "JSESSIONID" : "abclTvv8Wi3sgcxCfpUmw",
    #ick_login = 867db501-3f43-429e-8183-64c0b4b64b15;
    #jebecookies = f6017687-168b-426b-b488-a76324c95155|||||;
    #_de = 2A7EB32198D75E4E340E4CEC836F3769696BF75400CE19CC;
    #p = 24cdae0386bb784bb6df12416e03d9239;
    #first_login_flag = 1;
    #ln_uact = 384381523@qq.com;
    #ln_hurl = http://hdn.xnimg.cn/photos/hdn521/20111109/1300/h_main_8xSu_5f9300031a032f76.jpg;
    #t = cf7a01a6a311a306e1097e6fd43768299;
    #societyguester = cf7a01a6a311a306e1097e6fd43768299;
    #id = 336189169;
    #xnsid = d1bc232f;
    #loginfrom = syshome;
    #ch_id = 10016;
    #jebe_key = 5563c93d-9d49-4eef-8a89-3aca7d95045a%7C0d713231153ce535cf1ef2808c6c3b03%7C1525489595379%7C1%7C1525489596405;
    #wp_fold = 0
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies = self.cookies, callback = self.parse_page)
    def parse_page(self, response):
        print("==========" + response.url)
        with open("deng.html","w") as filename:
            filename.write(response.body)
