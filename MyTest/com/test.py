#!/usr/bin/python
#coding:utf8
'''
Created on 2015Äê12ÔÂ10ÈÕ

@author: liyutong
'''
import requests

r = requests.get("www.baidu.com")
print r.status_code