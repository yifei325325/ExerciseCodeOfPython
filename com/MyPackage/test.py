#!/usr/bin/python
#coding:utf8
'''
Created on 2015年12月22日

@author: Kenny.Li
'''
import socket
host = ""
port = 8888
for res in socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
print af
print socktype
print proto
print canonname
print sa
