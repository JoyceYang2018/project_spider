# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline

class ImagesPipeline(ImagesPipeline):
    #def process_item(self, item, spider):
    #   return item
    #获取settings文件里设置的变量值
    IMAGE_STORE = get_project_settings().get("IMAGE_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imagelink"]
        yield scrapy.Request(image_url)

    def item_completed(self, result, item, info):
         image_path = [x["path"] for ok, x in result if ok]
         os.rename(self.IMAGE_STORE +'/' + image_path[0], self.IMAGE_STORE + '/' + item["nickname"] + '.jpg')
         item["imagepath"] = self.IMAGE_STORE + '/' + item["nickname"]

         return item