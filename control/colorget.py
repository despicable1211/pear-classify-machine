# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colorget.ui'
#
# Created: Tue May 23 08:04:12 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from imageHandle import videoa
import numpy as np

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

class Ui_colorget(QtGui.QWidget):
    h1 = None
    s1 = None
    v1 = None
    h2 = None
    s2 = None
    v2 = None

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.camera = videoa()
        self.connect(self.camera, QtCore.SIGNAL('layoutLoadImage'), self.hhh)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(627, 438)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(157, 157, 157);"))
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(380, 80, 160, 19))
        self.horizontalSlider.setMaximum(179)
        self.horizontalSlider.setPageStep(13)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalSlider_2 = QtGui.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(380, 120, 160, 19))
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.horizontalSlider_3 = QtGui.QSlider(Form)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(380, 170, 160, 19))
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.horizontalSlider_4 = QtGui.QSlider(Form)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(380, 250, 160, 19))
        self.horizontalSlider_4.setMaximum(179)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.horizontalSlider_5 = QtGui.QSlider(Form)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(380, 300, 160, 19))
        self.horizontalSlider_5.setMaximum(255)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName(_fromUtf8("horizontalSlider_5"))
        self.horizontalSlider_6 = QtGui.QSlider(Form)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(380, 340, 160, 19))
        self.horizontalSlider_6.setMaximum(255)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName(_fromUtf8("horizontalSlider_6"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(430, 210, 41, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(430, 50, 51, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(550, 80, 64, 23))
        self.lcdNumber.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 127);"))
        self.lcdNumber.setProperty("value", 2.0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber_2 = QtGui.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(550, 120, 64, 23))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 0);"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.lcdNumber_3 = QtGui.QLCDNumber(Form)
        self.lcdNumber_3.setGeometry(QtCore.QRect(550, 170, 64, 23))
        self.lcdNumber_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 255);"))
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.lcdNumber_4 = QtGui.QLCDNumber(Form)
        self.lcdNumber_4.setGeometry(QtCore.QRect(550, 250, 64, 23))
        self.lcdNumber_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 127);"))
        self.lcdNumber_4.setObjectName(_fromUtf8("lcdNumber_4"))
        self.lcdNumber_5 = QtGui.QLCDNumber(Form)
        self.lcdNumber_5.setGeometry(QtCore.QRect(550, 300, 64, 23))
        self.lcdNumber_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 0);"))
        self.lcdNumber_5.setObjectName(_fromUtf8("lcdNumber_5"))
        self.lcdNumber_6 = QtGui.QLCDNumber(Form)
        self.lcdNumber_6.setGeometry(QtCore.QRect(550, 340, 64, 23))
        self.lcdNumber_6.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 255);"))
        self.lcdNumber_6.setObjectName(_fromUtf8("lcdNumber_6"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 331, 291))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 20, 321, 31))
        self.label_4.setStyleSheet(_fromUtf8(""))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 390, 561, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout.addWidget(self.pushButton_7)

        self.retranslateUi(Form)
        self.sliderConnent()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#0000ff;\">下界</span></p></body></html>", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#0000ff;\">上界</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#0000ff;\">HSV颜色范围拾取</span></p></body></html>", None))
        self.pushButton.setText(_translate("Form", "摄像头开", None))
        self.pushButton_2.setText(_translate("Form", "黄色", None))
        self.pushButton_3.setText(_translate("Form", "蓝色", None))
        self.pushButton_4.setText(_translate("Form", "红色", None))
        self.pushButton_5.setText(_translate("Form", "粉色", None))
        self.pushButton_6.setText(_translate("Form", "白色", None))
        self.pushButton_7.setText(_translate("Form", "退出", None))

    def sliderConnent(self):
        self.connect(self.horizontalSlider,QtCore.SIGNAL('valueChanged(int)'),self.changeValue1)
        self.connect(self.horizontalSlider_2, QtCore.SIGNAL('valueChanged(int)'), self.changeValue2)
        self.connect(self.horizontalSlider_3, QtCore.SIGNAL('valueChanged(int)'), self.changeValue3)
        self.connect(self.horizontalSlider_4, QtCore.SIGNAL('valueChanged(int)'), self.changeValue4)
        self.connect(self.horizontalSlider_5, QtCore.SIGNAL('valueChanged(int)'), self.changeValue5)
        self.connect(self.horizontalSlider_6, QtCore.SIGNAL('valueChanged(int)'), self.changeValue6)
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.openCamera1)
        self.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),self.yellowSave)
        self.connect(self.pushButton_3,QtCore.SIGNAL("clicked()"),self.blueSve)
        self.connect(self.pushButton_4,QtCore.SIGNAL("clicked()"),self.redSave)
        self.connect(self.pushButton_5,QtCore.SIGNAL("clicked()"),self.pinkSave)
        self.connect(self.pushButton_6,QtCore.SIGNAL("clicked()"),self.whiteSave)
        self.connect(self.pushButton_7,QtCore.SIGNAL("clicked()"),self.backTest)

    def changeValue1(self):
        self.h1 = self.horizontalSlider.value()
        self.lcdNumber.setProperty("value", self.h1)
        self.camera.H1 = self.h1

    def changeValue2(self):
        self.s1 = self.horizontalSlider_2.value()
        self.lcdNumber_2.setProperty("value", self.s1)
        self.camera.S1 = self.s1

    def changeValue3(self):
        self.v1 = self.horizontalSlider_3.value()
        self.lcdNumber_3.setProperty("value", self.v1)
        self.camera.V1 = self.v1

    def changeValue4(self):
        self.h2 = self.horizontalSlider_4.value()
        self.lcdNumber_4.setProperty("value", self.h2)
        self.camera.H2 = self.h2

    def changeValue5(self):
        s2 = self.horizontalSlider_5.value()
        self.lcdNumber_5.setProperty("value", s2)
        self.camera.S2 = s2

    def changeValue6(self):
        self.v2 = self.horizontalSlider_6.value()
        self.lcdNumber_6.setProperty("value", self.v2)
        self.camera.V2 = self.v2

    def openCamera1(self):
        print "摄像头测试"
        if(self.camera.stopa == 0):
            print "开始工作"
            self.pushButton.setText(_translate("Form", "摄像头关", None))
            self.camera.stopa = 1
            self.camera.start()
        else:
            print "停止工作"
            self.pushButton.setText(_translate("Form", "摄像头开", None))
            self.camera.stopa = 0

    def yellowSave(self):
        print "储存黄色HSV"
        self.camera.lower_yellow = np.array([self.h1,self.s1,self.v1])
        self.camera.upper_yellow = np.array([self.h2,self.s2,self.v2])

    def blueSve(self):
        print "储存蓝色HSV"
        self.camera.lower_blue = np.array([self.h1,self.s1,self.v1])
        self.camera.upper_blue = np.array([self.h2,self.s2,self.v2])

    def redSave(self):
        print "储存红色HSV"
        self.camera.lower_red = np.array([self.h1,self.s1,self.v1])
        self.camera.upper_red = np.array([self.h2,self.s2,self.v2])

    def pinkSave(self):
        print "储存粉色HSV"
        self.camera.lower_pink = np.array([self.h1,self.s1,self.v1])
        self.camera.upper_pink = np.array([self.h2,self.s2,self.v2])

    def whiteSave(self):
        print "储存白色HSV"
        self.camera.lower_white = np.array([self.h1,self.s1,self.v1])
        self.camera.upper_white = np.array([self.h2,self.s2,self.v2])

    def backTest(self):
        print "退出"

    def hhh(self, img):
        self.label_3.setPixmap(QtGui.QPixmap.fromImage(img))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QWidget()
    ui = Ui_colorget()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
