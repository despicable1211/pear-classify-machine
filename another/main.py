# -*- coding:utf-8 -*-
"""UI界面代码，按键函数在这里实现"""
import threading

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
        self.connect(self.thread, QtCore.SIGNAL('pearNumber'),self.updateNumber)
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

    #选择图片，即选择图片路径
    def loadInfo(self):
        self.thread.imagesrc = 1
        self.thread.imagepath = QtGui.QFileDialog.getOpenFileName(self, "open file dialog", "C:\Users\Administrator\Desktop",
                                            "Txt files(*.jpg)")
        self.testImage(self.thread.imagepath)
        print "导入图像处理"

    #打开图像处理子线程，开始处理数据
    def beginWork(self):
        self.thread.start()

    #进入另外一个界面
    def debugeng(self):
        print "进入调试"
        # self.form.close()
        Form1 = QtGui.QWidget()
        ui = Ui_widget()
        ui.setupUi(Form1)
        Form1.show()
        # Form1.exec_()
        self.form.show()

    #退出程序
    def exitSys(self):
        print "退出程序"
        self.close()

    def updateNumberhhh(self, pearNumber):
        self.updateNumber(pearNumber)

    def testImage(self,imagePath):
        imageTest = QtGui.QPixmap(imagePath)
        imageTest2 = imageTest.scaledToHeight(231)
        self.layoutLoadImage(imageTest2)

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
