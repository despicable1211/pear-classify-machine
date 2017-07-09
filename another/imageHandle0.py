# -*- coding:utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
import numpy as np
import cv2

class videoa(QtCore.QThread):
    stopa = 1 #线程开关标志位
    printInfo = 0 #打印信息标志位
    imagepath = None #图片路径
    imagesrc = 0 #图片来源
    listInfo = [0,0,0,0]
    sortInfo = 0

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.work_camera = 1

    def imageProcess(self,frame):
        path = str(frame)
        im = cv2.imread(path)
        # im = frame
        imageColor = im.copy()
        # 用低通滤波平滑图像
        result1 = cv2.blur(im,(5,5)) # dst = cv2.boxFilter(im, -1, (5, 5))  ;
        # 0 是指根据窗口大小（5,5）来计算高斯函数标准差
        # result1 = cv2.GaussianBlur(im, (5, 5), 0)
        imgray = cv2.cvtColor(result1, cv2.COLOR_BGR2GRAY)
        if(self.sortInfo == 3):
            ret, thresh = cv2.threshold(imgray, 127, 255,cv2.THRESH_TRUNC)#cv2.THRESH_TRUNC,0
        else:
            ret, thresh = cv2.threshold(imgray, 127, 255, 0)  # cv2.THRESH_TRUNC,0
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
            for i in range(list[0][0][1] + 10, list[0][0][1] + 15):  # 轮廓起始像素点往下5个点开始取像素行，取5行，避免边缘过渡像素的干扰
                for j in range(list[0][0][0] - 2, list[0][0][0] + 3):  # 取行往左2个，到右3个列的像素点
                    sumColorB = sumColorB + imageColor[i][j][0]  # 计算所有取到的像素点的B色值
                    sumColorG = sumColorG + imageColor[i][j][1]
                    sumColorR = sumColorR + imageColor[i][j][2]
            colorB = sumColorB / 25
            colorG = sumColorG / 25
            colorR = sumColorR / 25
            # 颜色判断
            color = 0
            if (colorR > 200 and colorG > 200 and colorB > 200):  # 白色
                color = 1
            elif (colorR > 245 and colorG < 40 and colorB < 35):  # 红色
                color = 2
            elif (colorR < 20 and colorG > 234 and colorB < 20):  # 绿色
                color = 3
            elif (colorR < 20 and colorG < 20 and colorB > 240):  #蓝色
                color = 4
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
            cv2.drawContours(im, contours, -1, (0, 255, 0), 2)
            self.listInfo[0] = area
            self.listInfo[1] = reat
            self.listInfo[2] = color
            return self.listInfo
            # cv2.line(im, (0, 0), (list[0][0][0]+3, list[0][0][1]+10), (0, 255, 0), 5)

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
        imageInfp = self.imageProcess(self.imagepath)
        step = self.select(imageInfp,self.sortInfo)
        # while self.stopa:
        #     print "判断光电开关信号，检测到开；并执行动作，动作完成后将stopa置0，结束线程"
