#!/usr/bin/python
#coding:utf8
'''
Created on 2015��12��10��

@author: liyutong
'''
import requests

r = requests.get("www.baidu.com")
print r.status_code