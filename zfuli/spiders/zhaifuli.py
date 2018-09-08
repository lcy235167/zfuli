# -*- coding: utf-8 -*-
import scrapy
import requests
import os
from bs4 import BeautifulSoup
from scrapy.selector import Selector
import re
import time
import random
from zfuli.items import ZfuliItem

class ZhaifuliSpider(scrapy.Spider):
    name = 'zhaifuli'
    #allowed_domains = ['https://52zfls.com']        
    start_urls = ["https://52zfls.com/luyilu/list_5_67.html"]
   
    
    def parse(self, response):
        articles = response.xpath('//div[@class="content"]//article')
        #print(articles[:1:])
        for article in articles:
            article_url = "https://52zfls.com" + article.xpath('./header/h2/a/@href').extract()[0]
#            title = article.xpath('./header/h2/a/text()')[0]
#            max_page = int(re.findall(r'\[(\d+)\w\]$', title)[0])
            
            for i in range(1, 32):
                time.sleep(1)
                if i == 1:
                    yield scrapy.Request(article_url, callback=self.parse_detail, dont_filter=True)    
                url = article_url[:-5] + '_' + str(i) + '.html'
                print('=========================================================')
                print(article_url)
                print(url)
                yield scrapy.Request(url, callback=self.parse_detail, dont_filter=True)
        next_page = response.xpath('//div[@class="content-wrap"]//div[@class="content"]\
                                   //div[@class="pagination pagination-multi"]/ul/li\
                                   [@class="next-page"]/a/@href')
        if next_page:
            next_page_url = "https://52zfl.vip/luyilu/" + next_page.extract()[0]
            yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)
    
    def parse_detail(self, response):
#        if response.url == "https://92zfl.com":
#            pass
#        else:    
        ps = response.xpath('//div[@class="content-wrap"]//div[@class="content"]//article//p')
        for p in ps:
            if p.xpath('./img/@src'):
                item = ZfuliItem()                                
                img_url = p.xpath('./img/@src').extract_first()
                name = re.search(r'/(\w+-\d+)\.jpg', img_url).group(1)
                print(img_url, name)
                time.sleep(1)
                item['name'] = name
                item['url'] = img_url
                yield item


#https://52zfls.com/luyilu/2016/1221/2744.html