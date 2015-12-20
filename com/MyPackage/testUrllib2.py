#!/usr/bin/python
#coding:utf8

'''
Created on 2015年12月18日

@author: Kenny.Li
'''
import urllib2,urllib

user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.1000 Chrome/30.0.1599.101 Safari/537.36"
values = {"username":"yifei1193@163.com","password":"csdn325325"}
headers1 = {"User-Agent":user_agent}
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# 
request = urllib2.Request(url,data,headers1)
print request.data
print request.get_method()
response = urllib2.urlopen(request)
# 
f = open("csdn.html",'w')
f.writelines(response.read())
f.close()
