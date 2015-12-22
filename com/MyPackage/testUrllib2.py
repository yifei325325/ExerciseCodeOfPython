#!/usr/bin/python
#coding:utf8

'''
Created on 2015年12月18日

@author: Kenny.Li
'''
import urllib2

url = 'http://blog.csdn.net/liyuanbhu/article/details/50365287'

my_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.1000 Chrome/30.0.1599.101 Safari/537.36',
                "Referer":"http://blog.csdn.net/",
                "Host":"blog.csdn.net",
                "GET":url
              }
#添加防爬网站必须的请求头
req = urllib2.Request(url,headers=my_headers)

html = urllib2.urlopen(req)
print html.read()
