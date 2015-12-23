#!/usr/bin/python
#coding:utf8
'''
Created on 2015年12月22日

@author: Kenny.Li
'''
import RNCryptor,base64

# s = raw_input("input the encrypted string:\n")
s = "AwFsMT4MseEK7S08non9ND3MghWLrkTzOxtpp+56xP4EpDOqeG4M1n1wsXOo/MNxzgn+fiDH81EmlN9rkdvFvX1r8Swfb33PKHfmhy95Fo83UP4CdgudRVl0/WChlA8QxquBtIlVSg4KfxlyyDRAHqIl9A7Z+qOrPZkBtnsphiFvbvwMlyRqpgMX3f85JRDLg9ICEaeqLZnaeMEtp3zsOUMRLZwRDPPVf496ujBwPYNWvD66lKtPbcz+2C/J9EF/yGxCcoih0FcLF5vzCrDhVbTlwb1zvlDXmFj63st8hmm6DtuoS+b6IBFjJuLJ+gbrIxncpqMG6wecQYopXn3dYQSjWezyvffESHbg55XlfmF1PG4RNAvk9tHB94H1lISX4bF1TLMe+dItIbCzrBPKFqBV"
pwd = "Cp2eWJAb"
r = RNCryptor.RNCryptor()

def jia_mi(s,pwd):
    return r.encrypt(s, pwd) 

def jie_mi(s,pwd):
    return r.decrypt(s, pwd)

print jie_mi(base64.decodestring(s), pwd)
print jia_mi("abc","abc")
