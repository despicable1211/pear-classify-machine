# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sun May 21 07:56:57 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
"""主UI界面代码，由PyQt自动生成"""

from PyQt4 import QtCore, QtGui

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
        Form.resize(619, 320)
        Form.setMinimumSize(QtCore.QSize(619, 320))
        Form.setMaximumSize(QtCore.QSize(619, 320))
        Form.setStyleSheet(_fromUtf8("background-color: rgb(185, 185, 185);"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 210, 91, 31))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(510, 250, 91, 31))
        self.pushButton_7.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(120, 50, 371, 231))
        self.label_7.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(517, 150, 81, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 170, 91, 31))
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 190, 91, 31))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 250, 91, 31))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 130, 91, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 91, 31))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(510, 40, 91, 111))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "广东海洋大学", None))
        self.label.setText(_translate("Form", "分类选择", None))
        self.pushButton_5.setText(_translate("Form", "手动调试", None))
        self.pushButton_7.setText(_translate("Form", "退出", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">珍 珠 分 拣 控 制 系 统</span></p></body></html>", None))
        self.pushButton_6.setText(_translate("Form", "开始", None))
        self.pushButton_3.setText(_translate("Form", "颜色", None))
        self.pushButton_4.setText(_translate("Form", "导入图像", None))
        self.pushButton_2.setText(_translate("Form", "圆度", None))
        self.pushButton.setText(_translate("Form", "大小", None))
        self.label_2.setText(_translate("Form", "总数", None))
        self.label_5.setText(_translate("Form", "0", None))
        self.label_3.setText(_translate("Form", "良品数", None))
        self.label_6.setText(_translate("Form", "0", None))

    def layoutLoadImage(self,image):#更新layout显示图像
        self.label_7.setPixmap(image)#(QtGui.QPixmap(image))

    def updateNumber(self,number):#更新数量layout显示
        self.label_5.setText(_translate("Form", str(number), None))
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
