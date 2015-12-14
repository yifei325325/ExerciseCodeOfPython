#!/usr/bin/Python
#coding:utf8

import time

i = 1
try:
    while 1:
        print "haha",i
        i += 1
        time.sleep(2)
except KeyboardInterrupt,e:
    print "end"
    print e
    
print "main thread end"