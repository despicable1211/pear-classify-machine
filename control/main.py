# -*- coding:utf-8 -*-
import threading
"""主界面函数"""

from PyQt4 import QtGui
from PyQt4 import QtCore
# from PyQt4.QtGui import QFileDialog

from ui_name import Ui_Form
from imageHandle import videoa
from my_ui import Ui_widget
import cv2

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Widget(QtGui.QWidget,Ui_Form):
    thread = None
    thread_camera = 0
    number = 0
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.setupUi(self)
        self.thread = videoa()
        self.connect(self.thread, QtCore.SIGNAL('layoutLoadImage'),self.hhh)#信号槽设置，将收到信号后连接到指定的函数
        self.buttonDefine()

    # 信号连接到指定槽
    def buttonDefine(self):
        self.pushButton.clicked.connect(self.setSize)
        self.pushButton_2.clicked.connect(self.setCount)
        self.pushButton_3.clicked.connect(self.setColor)
        self.pushButton_4.clicked.connect(self.loadInfo)
        self.pushButton_6.clicked.connect(self.beginWork)
        self.pushButton_5.clicked.connect(self.debugeng)
        self.pushButton_7.clicked.connect(self.exitSys)

    def setSize(self):
        print "设置大小"
        self.thread.sortInfo = 1

    def setCount(self):
        print "设置圆度"
        self.thread.sortInfo = 2

    def setColor(self):
        print "设置颜色"
        self.thread.sortInfo = 3

    def loadInfo(self):
        print "导入图像处理"
        self.thread.printInfo=1

    def beginWork(self):
        if(self.thread.stopa == 0):
            print "开始工作"
            self.pushButton_6.setText(_translate("Form", "开始", None))
            self.thread.stopa = 2
            self.thread.start()
        else:
            print "停止工作"
            self.pushButton_6.setText(_translate("Form", "开始", None))
            self.thread.stopa = 0

    def debugeng(self):
        print "进入调试"
        # self.form.close()
        Form1 = QtGui.QWidget()
        ui = Ui_widget()
        ui.setupUi(Form1)
        Form1.show()
        # Form1.exec_()
        self.form.show()

    def exitSys(self):
        print "退出程序"
        self.close()

    def hhh(self, img):#设置图像显示
        self.layoutLoadImage(img)

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
