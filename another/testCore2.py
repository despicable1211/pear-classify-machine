# -*- coding: utf-8 -*-

import cv2
# from PyQt4 import QtGui
#
# cameraCapture = cv2.VideoCapture(0)
# cv2.namedWindow('mywindow')
# success,frame = cameraCapture.read()
# cv2.imwrite("test.jpg",frame)
# while success and cv2.waitKey(1) == -1:
#     cv2.imshow('mywindow',frame)
#
#     success,frame = cameraCapture.read()
#
#
# cv2.destroyWindow('mywindow')
# cameraCapture.release()
image=cv2.imread('606.jpg')
res=cv2.resize(image,(32,32),interpolation=cv2.INTER_CUBIC)
cv2.imshow('iker',res)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destoryAllWindows()