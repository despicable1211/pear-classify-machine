# -*- coding:utf-8 -*-
"""图像处理、分类控制代码代码，出界面外的所以代码在此实现"""
from PyQt4 import QtGui
from PyQt4 import QtCore
import numpy as np
import cv2
import RPi.GPIO as GPIO
import time
from stepControl import stepControl

class videoa(QtCore.QThread):
    stopa = 1            #线程开关标志位，简单的结束线程里的while循环
    printInfo = 0
    imagepath = None     #图片路径
    imagesrc = 0         #图片来源
    listInfo = [0,0,0,0] #处理完后得到的图像信息保留在这个列表里面
    sortInfo = 0         #处理图像类型标志位，默认为0，即不出来图像。需要先选择分类类型
    pearNumber = 0

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.work_camera = 1

    def imageProcess(self,frame):

        path = str(frame)#将路径转换成字符串

        im = cv2.imread(path)#读取图片

        imageColor = im.copy()#复制源图像，用于后续颜色检测，因为后续的处理会在覆盖在处理的图像上

        result1 = cv2.blur(im,(5,5))# 用低通滤波平滑图像 # dst = cv2.boxFilter(im, -1, (5, 5))  ;
        # 0 是指根据窗口大小（5,5）来计算高斯函数标准差
        # result1 = cv2.GaussianBlur(im, (5, 5), 0)


        imgray = cv2.cvtColor(result1, cv2.COLOR_BGR2GRAY)#图片灰度处理
        #分为两部分，测试过程中发现，对于彩色图片和黑白图片，不能用同一个参数二值化。故分为彩色和其它，如果是实时图像处理，二值化函数必须要统一，这里在实时处理中要改变
        if(self.sortInfo == 3):
            ret, thresh = cv2.threshold(imgray, 127, 255,cv2.THRESH_TRUNC)#二值化。cv2.THRESH_TRUNC,0
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)#检测轮廓
        else:
            ret, thresh = cv2.threshold(imgray, 127, 255, 0)  # 二值化。cv2.THRESH_TRUNC,0
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)#检测轮廓

        if contours:#判断是否取到轮廓，如果取到进入后续处理

            cnt = contours[0]# 取第 0 个轮廓

            rect = cv2.minAreaRect(cnt)# 计算最小包围矩形

            # box = cv2.boxPoints(rect)# 矩形四个顶点坐标

            rectBoard = rect[1]# 取矩形边长列表

            # 取长短直径，并判断圆度
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

                reat = ((longDiameter - shortDiameter) / shortDiameter) * 100# 用最短直径/最长直径求圆度

            area = cv2.contourArea(cnt) # 计算轮廓面积

            list = np.ndarray.tolist(cnt)# 将轮廓的ndarray类型转换为Python的list类型

            coloList = np.ndarray.tolist(imageColor) # 将原图像的ndarray类型数据转为Python类型数据

            # 计算5*5个像素点三原色
            sumColorB = 0
            sumColorG = 0
            sumColorR = 0
            for i in range(list[0][0][1] + 10, list[0][0][1] + 15):  # 轮廓起始像素点往下10个点开始取像素行，取5行，避免边缘过渡像素的干扰
                for j in range(list[0][0][0] - 2, list[0][0][0] + 3):  # 取行往左2个，到右3个列的像素点
                    sumColorB = sumColorB + imageColor[i][j][0]  # 计算所有取到的像素点的B色值
                    sumColorG = sumColorG + imageColor[i][j][1]
                    sumColorR = sumColorR + imageColor[i][j][2]
            colorB = sumColorB / 25
            colorG = sumColorG / 25
            colorR = sumColorR / 25

            # 颜色判断，颜色范围根据需要实验数据设置
            color = 0
            if (colorR > 200 and colorG > 200 and colorB > 200):  # 白色
                color = 1
            elif (colorR > 245 and colorG < 40 and colorB < 35):  # 红色
                color = 2
            elif (colorR < 20 and colorG > 234 and colorB < 20):  # 绿色
                color = 3
            elif (colorR < 20 and colorG < 20 and colorB > 240):  #蓝色
                color = 4

            #打印处理完的图像信息
            if(self.printInfo == 0):
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
                    print "检测颜色为：" + "绿色"
                elif(color==4):
                    print "检测颜色为：" + "蓝色"
                else:
                    print "检测颜色为失败"
                self.printInfo=0

            cv2.drawContours(im, contours, -1, (0, 255, 0), 2)#用绿色绘制轮廓边缘

            self.listInfo[0] = area
            self.listInfo[1] = reat
            self.listInfo[2] = color
            return self.listInfo
            # cv2.line(im, (0, 0), (list[0][0][0]+3, list[0][0][1]+10), (0, 255, 0), 5)

    #分类函数，根据采集到的信息设置步进电机步距。@param1：图像信息列表 @param：分类类型
    def select(self,imafotion,sortInfo):
        step = 0
        if(sortInfo == 1):  #按大小
            if (imafotion[0] <1500):  # 面积1
                print "面积小于1500"
                step = -80
            elif (imafotion[0] >=1500 and imafotion[0] <3000):  # 面积2
                print "面积1500-300"
                step = -15
            elif (imafotion[0] >=3000 and imafotion[0] <5000):  # 面积3
                print "面积3000-5000"
                step = 43
            elif (imafotion[0] >=5000):  # 面积4
                print "面积大于5000"
                step = 110
        elif(sortInfo == 2):    #按圆度
            if (imafotion[1] <1):  # 圆度1
                print "正圆"
                step = 110
            elif (imafotion[1] >=1 and imafotion[1] <5):  # 圆度2
                print "圆"
                step = 43
            elif (imafotion[1] >=5 and imafotion[1] <10):  # 圆度3
                print "近圆"
                step = -15
            elif (imafotion[1] >=10):  # 圆度4
                print "不圆"
                step = -80
        elif(sortInfo == 3):    #按颜色
            if (imafotion[2] == 1):    # 白色
                print "白色步距"
                step = 110
            elif (imafotion[2] == 2):  # 红色
                print "红色步距"
                step = 43
            elif (imafotion[2] == 3):  # 绿色
                print "绿色步距"
                step = -15
            elif (imafotion[2] == 4):  # 蓝色
                print "蓝色步距"
                step = -80
        return step

    def run(self):
        imageInfp = self.imageProcess(self.imagepath)#图像处理
        step = self.select(imageInfp,self.sortInfo)#步距设置

        #初始化所有关于IO口的设置
        stepclass = stepControl()
        stepclass.setup()
        stepclass.setStep(0,0,0,0)
        GPIO.setup(12,GPIO.IN,pull_up_down = GPIO.PUD_UP)

        while True and step:
            if(GPIO.input(12) == GPIO.LOW):#光电开关信号检测
                self.pearNumber +=1#珍珠数量统计
                self.emit(QtCore.SIGNAL("pearNumber"), self.pearNumber)#发送珍珠数量信号
                print step
                stepclass.motorGO(step) #控制步进电机
                step = 0
        # while self.stopa:
        #     print "判断光电开关信号，检测到开；并执行动作，动作完成后将stopa置0，结束线程"
