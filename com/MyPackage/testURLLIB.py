#!/usr/bin/python
#coding:utf8
'''
Created on 2015年12月20日

@author: kenny.li
'''
import urllib,chardet

def auto_detect(url):
    content = urllib.urlopen(url).read() 
    result = chardet.detect(content)
    encoding = result['encoding']
    return encoding
 
urls = ['http://www.baidu.com',
        'http://www.sina.com.cn',
        'http://www.jd.com',
        'http://www.taobao.com',
        'http://www.ibabycloud.com',
        ]
 
for url in urls:
    print url,'\t',auto_detect(url)
#************************************************
# url = "http://www.baidu.com"
