#coding:utf8
'''
Created on 2015年12月24日

@author: Kenny.Li

pyQt 写的一个小窗体
'''
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250,150)
widget.setWindowTitle("My Simple")
widget.show()

sys.exit(app.exec_())
