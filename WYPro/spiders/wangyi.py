# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://news.163.com']

    def __init__(self):
        # 放在这边为了只实例化一次webdriver对象

        self.bro = webdriver.Chrome(executable_path=r"C:\Users\92037\Desktop\chromedriver")

    # 保证浏览器的关闭在整个爬虫结束之后

    def closed(self, spider):
        print('爬虫结束')
        self.bro.quit()

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

            yield  scrapy.Request(url=url, callback=self.parseSecond)

    def parseSecond(self, response):
        div_list = response.xpath('//div[@class="data_row news_article clearfix "]')
        print(len(div_list))

        for div in div_list:
            head = div.xpath('.//div[@class=news_title]/h3/a/text()').extract_first()
            url = div.xpath('.//div[@class=news_title]/h3/a/@href').extract_first()
            imageUrl = div.xpath('./a/img/@src').extract_first()
            tagList = div.xpath('.//div[@class="news_tag"]//text()').extract()
            tag = ''.join(tagList)