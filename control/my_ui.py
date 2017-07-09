# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_ui.ui'
#
# Created: Sun May 21 07:48:57 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from imageHandle import videoa

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

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName(_fromUtf8("widget"))
        self.foo = widget
        widget.resize(619, 320)
        widget.setMinimumSize(QtCore.QSize(619, 320))
        widget.setMaximumSize(QtCore.QSize(619, 320))
        widget.setStyleSheet(_fromUtf8("background-color: rgb(175, 175, 175);"))
        self.label = QtGui.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(40, 10, 531, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 81, 31))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(widget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 150, 81, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(widget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 90, 81, 31))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(widget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 150, 81, 31))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(widget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 200, 81, 31))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(widget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 200, 81, 31))
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(widget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 260, 81, 31))
        self.pushButton_7.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_2 = QtGui.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(240, 60, 361, 231))
        self.label_2.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(0, 0, 0);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_8 = QtGui.QPushButton(widget)
        self.pushButton_8.setGeometry(QtCore.QRect(130, 260, 81, 31))
        self.pushButton_8.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.label_3 = QtGui.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(60, 50, 101, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(widget)
        self.buttonDefine()

        #信号槽设置，将收到信号后处理对应函数
        self.thread = videoa()
        self.bcd = QtGui.QWidget
        self.bcd.connect(self.thread, QtCore.SIGNAL('layoutLoadImage'),self.hhh)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        widget.setWindowTitle(_translate("widget", "广东海洋大学", None))
        self.label.setText(_translate("widget", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">珍 珠 分 拣 控 制 系 统</span></p></body></html>", None))
        self.pushButton.setText(_translate("widget", "步进放料", None))
        self.pushButton_2.setText(_translate("widget", "梭子放料", None))
        self.pushButton_3.setText(_translate("widget", "光电开关1", None))
        self.pushButton_4.setText(_translate("widget", "光电开关2", None))
        self.pushButton_5.setText(_translate("widget", "摄像头测试开", None))
        self.pushButton_6.setText(_translate("widget", "A区放料", None))
        self.pushButton_7.setText(_translate("widget", "B区放料", None))
        self.pushButton_8.setText(_translate("widget", "返回", None))
        self.label_3.setText(_translate("widget", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#0000ff;\">手动调试</span></p></body></html>", None))

    def hhh(self,image):
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))

    def buttonDefine(self):
        # 信号连接到指定槽
        self.pushButton.clicked.connect(self.step_feeding)
        self.pushButton_2.clicked.connect(self.shuttle_discharge)
        self.pushButton_3.clicked.connect(self.photoelectric_switch_1)
        self.pushButton_4.clicked.connect(self.photoelectric_switch_2)
        self.pushButton_5.clicked.connect(self.camera)
        self.pushButton_6.clicked.connect(self.A_zone_feeding)
        self.pushButton_7.clicked.connect(self.B_zone_feeding)
        self.pushButton_8.clicked.connect(self.comback)

    def step_feeding(self):
        print "步进放料"

    def shuttle_discharge(self):
        print "梭子放料"

    def photoelectric_switch_1(self):
        print "光电开关1"

    def photoelectric_switch_2(self):
        print "光电开关2"

    def camera(self):
        print "摄像头1"
        if(self.thread.stopa == 0):
            print "开始工作"
            self.pushButton_5.setText(_translate("Form", "摄像头测试关", None))
            self.thread.stopa = 3
            self.thread.start()
        else:
            print "停止工作"
            self.pushButton_5.setText(_translate("Form", "摄像头测试开", None))
            self.thread.stopa = 0

    def A_zone_feeding(self):
        print "A区放料"

    def B_zone_feeding(self):
        print "B区放料"

    def comback(self):
        self.foo.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QWidget()
    ui = Ui_widget()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
