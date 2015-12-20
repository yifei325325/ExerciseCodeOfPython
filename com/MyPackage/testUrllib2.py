#!/usr/bin/python
#coding:utf8

'''
Created on 2015年12月18日

@author: Kenny.Li
'''
import urllib2,urllib

url = 'http://blog.csdn.net/liyuanbhu/article/details/50365287'
req = urllib2.Request(url)

#添加防爬网站必须的请求头
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.1000 Chrome/30.0.1599.101 Safari/537.36')
req.add_header("Referer","http://blog.csdn.net/")
req.add_header("Host","blog.csdn.net")
req.add_header("GET",url)

html = urllib2.urlopen(req)
print html.read()
