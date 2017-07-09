# -*- coding:utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
import numpy as np
import cv2

class videoa(QtCore.QThread):
    cv2Video = None
    stopa = 0 #线程开关标志位
    printInfo = 0 #打印信息标志位
    imagepath = None #图片路径
    imagesrc = 0 #图片来源
    sortInfo = 0
    H1 = 110
    S1 = 50
    V1 = 50
    H2 = 130
    S2 = 255
    V2 = 255
    lower_red = np.array([155,128,118])
    upper_red = np.array([179,255,197])
    lower_yellow = np.array([14,228,74])
    upper_yellow = np.array([47,255,255])
    lower_white = np.array([82,0,135])
    upper_white = np.array([123,56,176])
    lower_blue = np.array([100,122,98])
    upper_blue = np.array([120,188,171])
    lower_pink = np.array([123,26,86])
    upper_pink = np.array([163,92,140])

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.work_camera = 1

    def imageProcess(self,frame):
        # im = cv2.imread(frame)
        im = frame
        imageColor = im.copy()
        # 用低通滤波平滑图像
        result1 = cv2.blur(im,(5,5)) # dst = cv2.boxFilter(im, -1, (5, 5))  ;
        # 0 是指根据窗口大小（5,5）来计算高斯函数标准差
        # result1 = cv2.GaussianBlur(im, (5, 5), 0)
        imgray = cv2.cvtColor(result1, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        if contours:
            # 取第 0 个轮廓
            cnt = contours[0]
            # 计算最小包围矩形
            rect = cv2.minAreaRect(cnt)
            # 矩形四个顶点坐标
            # box = cv2.boxPoints(rect)
            # 取矩形边长列表
            rectBoard = rect[1]
            # 取长短直径
            reat = 0
            shortDiameter = 0
            longDiameter = 0
            if(rectBoard[0] and rectBoard[1]):
                if (rectBoard[1] > rectBoard[0]):
                    shortDiameter = rectBoard[0]
                    longDiameter = rectBoard[1]
                else:
                    longDiameter = rectBoard[0]
                    shortDiameter = rectBoard[1]
                # 用最短直径/最长直径求圆度
                reat = ((longDiameter - shortDiameter) / shortDiameter) * 100
            # 计算轮廓面积
            area = cv2.contourArea(cnt)
            # 将轮廓的ndarray类型转换为Python的list类型
            list = np.ndarray.tolist(cnt)
            # 将原图像的ndarray类型数据转为Python类型数据
            coloList = np.ndarray.tolist(imageColor)
            # 计算5*5个像素点三原色
            sumColorB = 0
            sumColorG = 0
            sumColorR = 0
            color = 0
            if(len(cnt)>100):
                for i in range(list[0][0][1] + 10, list[0][0][1] + 15):  # 轮廓起始像素点往下5个点开始取像素行，取5行，避免边缘过渡像素的干扰
                    for j in range(list[0][0][0] - 2, list[0][0][0] + 3):  # 取行往左2个，到右3个列的像素点
                        sumColorB = sumColorB + imageColor[i][j][0]  # 计算所有取到的像素点的B色值
                        sumColorG = sumColorG + imageColor[i][j][1]
                        sumColorR = sumColorR + imageColor[i][j][2]
                colorB = sumColorB / 25
                colorG = sumColorG / 25
                colorR = sumColorR / 25
                # 颜色判断
                if (colorR > 200 and colorG > 200 and colorB > 200):  # 白色
                    color = 1
                elif (colorR > 245 and colorG < 40 and colorB < 35):  # 红色
                    color = 2
                elif (colorR > 243 and colorG > 234 and colorB < 110):  # 黄色
                    color = 3
            if(self.printInfo == 1):
                print "面积是" + str(area)
                print "最长直径" + str(longDiameter)
                print "最短直径" + str(shortDiameter)
                print "圆度" + str(reat) + "%"
                print "轮廓点数：" + str(len(cnt)) + "     检测到" + str(len(contours)) + "个轮廓"
                print "轮廓起始点" + str(list[0])
                print "图片行：" + str(len(coloList)) + ";" + "图片列：" + str(len(coloList[0]))
                print "三原色：" + "B " + str(colorB) + "  G "+ str(colorG) + " R " + str(colorR)
                if(color==1):
                    print "检测颜色为：" + "白色"
                elif(color==2):
                    print "检测颜色为：" + "红色"
                elif(color==3):
                    print "检测颜色为：" + "黄色"
                else:
                    print "检测颜色为失败"
                self.printInfo=0
            cv2.drawContours(im, contours, -1, (0, 255, 0), 2)
        listInfo = [0, 0, 0, 0]
        listInfo[0] = area
        listInfo[1] = reat
        listInfo[2] = color
        return listInfo
    #         # cv2.line(im, (0, 0), (list[0][0][0]+3, list[0][0][1]+10), (0, 255, 0), 5)
    #         # cv2.imshow('detected circles', im)
    def select(self,imafotion,sortInfo):
        step = 0
        if(sortInfo == 1):  #按大小
            if (imafotion[0] <1500):  # 面积1
                print "面积小于1500"
                step = 50
            elif (imafotion[0] >=1500 and imafotion[0] <3000):  # 面积2
                print "面积1500-300"
                step = 100
            elif (imafotion[0] >=3000 and imafotion[0] <5000):  # 面积3
                print "面积3000-5000"
                step = 15
            elif (imafotion[0] >=5000):  # 面积4
                print "面积大于5000"
                step = 0
        elif(sortInfo == 2):    #按圆度
            if (imafotion[1] <1):  # 圆度1
                print "正圆"
                step = 0
            elif (imafotion[1] >=1 and imafotion[1] <5):  # 圆度2
                print "圆"
                step = 50
            elif (imafotion[1] >=5 and imafotion[1] <10):  # 圆度3
                print "近圆"
                step = 100
            elif (imafotion[1] >=10):  # 圆度4
                print "不圆"
                step = 100
        elif(sortInfo == 3):    #按颜色
            if (imafotion[2] == 1):    # 白色
                print "白色步距"
                step = 0
            elif (imafotion[2] == 2):  # 红色
                print "红色步距"
                step = 25
            elif (imafotion[2] == 3):  # 绿色
                print "绿色步距"
                step = 50
            elif (imafotion[2] == 4):  # 蓝色
                print "蓝色步距"
                step = 110
        return step
    def run(self):
        cv2Video = cv2.VideoCapture(0)
        success, frame = cv2Video.read()
        loopNumber = 0
        while success and self.stopa > 0:
            success, frame = cv2Video.read()
            if(self.stopa == 1):
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                lower_blue = np.array([self.H1, self.S1, self.V1])
                upper_blue = np.array([self.H2, self.S2,self.V2])
                mask = cv2.inRange(hsv, lower_blue, upper_blue)
                cv2.imshow("mask", mask)
                res = cv2.bitwise_and(frame, frame, mask=mask)
                height, width, bytesPerComponent = res.shape
                bytesPerLine = 3 * width
                cv2.cvtColor(res, cv2.COLOR_BGR2RGB, res)
                qImage = QtGui.QImage(res.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                newQimage = qImage.scaledToWidth(371)
            if(self.stopa == 2):
                if(loopNumber>10):
                    listInfo = self.imageProcess(frame)
                    self.select(listInfo, self.sortInfo)
                    if(loopNumber>100):
                        loopNumber = 20
                loopNumber += 1
                #转化到QT显示格式
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = 3 * width
                cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
                qImage = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                # newQimage = qImage.scaledToWidth(371) #使用图像宽度
                newQimage = qImage.scaledToHeight(231)  #使用图像高度

            self.emit(QtCore.SIGNAL("layoutLoadImage"), newQimage)
        cv2Video.release()
        print "关闭摄像头线程"
