# -*- coding: utf-8 -*-
import scrapy


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://news.163.com']

    def parse(self, response):
        lis = response.xpath('//div[@class="ns_area list"]/ul/li')
        indexs = [3, 4, 6, 7]
        # 这个列表里边存储就是对应板块的标签对象
        li_list = []
        for index in indexs:
            li_list.append(lis[index])
        # 获取四个板块中的超链接,和文字标题
        for li in li_list:
            # 拿到url
            url = li.xpath('./a/@href').extract_first()
            # 拿到板块标题
            title = li.xpath('./a/text()').extract_first()

            print(url+':'+title)