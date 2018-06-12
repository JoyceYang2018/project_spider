# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import base64
from settings import USER_AGENTS
from settings import PROXIES
from scrapy import signals

#随机的User_Agent
class RandomUserAgent(object):
    def process_request(self,request,spider):
        useragent = random.choice(USER_AGENTS)
        #print useragent
        request.headers.setdefault("User-Agent",useragent)

class RandomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXIES)

        if proxy['user_passwd'] is None:
            #如果没有代理账户验证的代理使用方式
            request.meta['proxy'] = "http://" + proxy['ip_port']
        else:
            base64_userpasswd = base64.b64decode(proxy['user_passwd'])
            request.headers['Proxy-Authorization'] = 'Basic '+ base64_userpasswd
            request.meta['proxy'] = "http://" + proxy['ip_port']
