#coding:utf8
'''
Created on 2015年12月24日

@author: Kenny.Li
'''

import sys
from PyQt4 import QtGui
class Icon(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        
        self.setGeometry(50,50,500,400)
        self.setWindowTitle("Icon")
        i = QtGui.QIcon("icons/snowman.png")
        self.setWindowIcon(i)

app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())