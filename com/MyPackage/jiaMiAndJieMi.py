#!/usr/bin/python
#coding:utf8
'''
Created on 2015年12月22日

@author: Kenny.Li
'''
import RNCryptor

s = "test"
pwd = "mypwd"
r = RNCryptor.RNCryptor()

def jia_mi(s,pwd):
    return r.encrypt(s, pwd) 

def jie_mi(s,pwd):
    return r.decrypt(s, pwd)

print u"原字串:\t",s
print u"加密后:\t",jia_mi(s, pwd)
print u"解密后:\t",jie_mi(jia_mi(s, pwd), pwd)