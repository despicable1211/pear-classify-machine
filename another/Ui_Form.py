# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Wed May 17 11:41:58 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(612, 312)

        #media play
        self.videoPlayer = phonon.Phonon.VideoPlayer(Form)
        self.videoPlayer.setGeometry(QtCore.QRect(109, 39, 391, 251))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        # self.videoPlayer.load(phonon.Phonon.MediaSource("Wildlife.wmv"))
        # self.videoPlayer.play()
        self.label = QtGui.QLabel(Form)

        #set windows
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        #button control
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 91, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 170, 91, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 220, 91, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 210, 91, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 160, 91, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(510, 250, 91, 31))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(530, 40, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(520, 100, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(520, 70, 54, 12))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(520, 130, 54, 12))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "广东海洋大学", None))
        self.label.setText(_translate("Form", "分类选择", None))
        self.pushButton.setText(_translate("Form", "大小", None))
        self.pushButton_2.setText(_translate("Form", "圆度", None))
        self.pushButton_3.setText(_translate("Form", "颜色", None))
        self.pushButton_4.setText(_translate("Form", "导入", None))
        self.pushButton_5.setText(_translate("Form", "手动调试", None))
        self.pushButton_6.setText(_translate("Form", "光电开关测试", None))
        self.pushButton_7.setText(_translate("Form", "退出", None))
        self.label_2.setText(_translate("Form", "总数", None))
        self.label_3.setText(_translate("Form", "良品数", None))
        self.label_4.setText(_translate("Form", "珍 珠 分 拣 控 制 系 统", None))
        self.label_5.setText(_translate("Form", "0", None))
        self.label_6.setText(_translate("Form", "0", None))

    def loadVidei(self,video):
        self.videoPlayer.load(phonon.Phonon.MediaSource(video))
        self.videoPlayer.play()
from PyQt4 import phonon
