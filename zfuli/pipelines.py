# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from hashlib import md5
import requests
import random
import time

headers = [
           {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"},
           {"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
           {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
           {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"},
           {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"},
           {"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"},
           {"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"},
           {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
           {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
           {"User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"}
    ]
data = {"authority":"52zfls.com",
"if-modified-since":"Mon, 03 Sep 2018 09:28:09 GMT",
"if-none-match":"W/a859ca6d6843d41:0",
"upgrade-insecure-requests":"1",
"cookie":"UM_distinctid=164dfa450c05ed-047a91a5fe3438-62381459-144000-164dfa450c16e0; ASPSESSIONIDSQADDSDD=NJDNNNCDIJLFBDEIEFMHEGKH; CNZZDATA1254428444=25510713-1532755052-%7C1536115168; Hm_lvt_731a53a94394c1764ce2ab6cc1a76d2d=1535593689,1535981860,1536044111,1536115905; Hm_lpvt_731a53a94394c1764ce2ab6cc1a76d2d=1536116260"}


class ZfuliPipeline(object):
    def process_item(self, item, spider):
        
#        with open('tencent.json','ab') as f:
#            text = json.dumps(dict(item), ensure_ascii=False)+'\n'
#            f.write(text.encode('utf-8'))
        url = item['url']
        name = item['name']
        try:
            
            print(url, name)
            r = requests.get(url, headers=random.choice(headers).update(data), allow_redirects=False)
            print(r.status_code)
            if r.status_code == 200:    
                with open("D:\Mzitu\\" + name + ".jpg", 'ab') as f:
                    f.write(r.content)
                    print("OK")
                return item
            with open("Mzituerr.txt", 'a') as f:
                f.write(url + '\n')
                return item
        except:
            with open("Mzituerr.txt", 'a') as f:
                f.write(url + '\n')
                return item





