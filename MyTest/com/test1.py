#-*-coding:utf8-*-
'''
Created on 2015年12月9日

@author: liyutong
'''
import win32api as w
import os

# w.Beep(500,500)
w.ShellExecute(0,'open',r'F:\KuGou\Amy Diamond - Heartbeats.mp3','','',1)

f = open('content','r')
command = f.read().split("#")
print command
if command != '0':
    w.MessageBox(0,command[1].decode('utf8'),command[2].decode('utf8')) 
    os.system("shutdown -s -t 300")
    # os.system("shutdown -a")
    

    
    

