#!/usr/bin/python
#coding:utf8
'''
Created on 2015年12月19日

@author: kenny.li
'''
s = "中文"  #因为我的编辑器默认的编码方式是utf-8
print "s = ",s  #所以我直接打印，可以正常显示中文，但是在print "s_new = ",s_new的时候会是乱码
s_new = s.decode("utf8").encode("gbk")#我将S先用utf-8编码方式解码成unicode编码，再encode编码成“gbk”编码
print "s_new = ",s_new #因为前一步的操作，所以我这里打印出来的结果是有乱码的

