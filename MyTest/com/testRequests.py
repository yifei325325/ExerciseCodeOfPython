#!/usr/bin/python
#coding:utf8
'''
Created on 2015年12月10日

@author: liyutong
'''
import requests,time

url = 'http://www.ibabyclouds.com'
try:
    r = requests.get(url)
    if r.status_code == 200:
        print "服务器返回'%d',网络连接正常！" %r.status_code
        try:
            f = open('log.txt','w')
            f.writelines(r.text.encode('utf8'))
            f.close()
            print '返回的html源码请看log.txt'
        except Exception,e:
            print e
    else:
        print 'r.status_code:',r.status_code
except Exception,e:
    print time.strftime('%H:%M:%S',time.localtime()),'\t',e
    print '%s\twrong address'%time.strftime('%H:%M:%S',time.localtime())

  
