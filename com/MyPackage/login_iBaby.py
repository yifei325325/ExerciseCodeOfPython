#!/usr/bin/python
#coding:utf8
'''
Created on 2015年12月22日

@author: Kenny.Li
'''
import urllib2,urllib

url = "http://www.ibabycloud.com/api/v1/user/login"
my_headers = {'User-Agent':'iBaby Care 1.1.2 rv:20151215101 (iPhone; iPhone OS 9.2; en_CN)'}
name_pwd = {"username":"test12@163.com","password":"123456"}
data = urllib.urlencode(name_pwd)

req = urllib2.Request(url,data,my_headers)
con = urllib2.urlopen(req)
