# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class OrderInfo(models.Model):
    oid=models.CharField(max_length=20,primary_key=True)
    user=models.ForeignKey('df_user.UserInfo')
    odate=models.DateTimeField(auto_now=True)
    oIsPay=models.BooleanField(default=False)
    otatal=models.DecimalField(max_digits=6,decimal_places=2)
    #otatal其实市可以由orderdetail中的商品数量价格等计算出来，算是冗余数据，但是用聚合计算的话，每次计算总数都需要调用数据库，使用频率较高，增加服务器压力，所以这里定义一个变量作为冗余保存这个值。
    oaddress=models.CharField(max_length=150)
    #无法实现：物流信息，真实支付
class OrderDetailInfo(models.Model):
    goods=models.ForeignKey('df_goods.GoodInfo')
    order=models.ForeignKey(OrderInfo)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    count=models.IntegerField()