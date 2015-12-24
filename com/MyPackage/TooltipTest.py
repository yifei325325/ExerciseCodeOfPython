#coding:utf8
'''
Created on 2015年12月24日

@author: Kenny.Li
'''
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Tooltip(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle(u"工具提示")
        self.setToolTip(u"这是一个 <b>QWidget</b> 框架写的窗体")
        QtGui.QToolTip.setFont(QtGui.QFont("OldEnglish",10))
        
app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())