# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CartInfo(models.Model):
    user=models.ForeignKey('df_user.UserInfo')
    goods=models.ForeignKey('df_goods.GoodInfo')
    count=models.IntegerField()
    #谁买了几个什么
