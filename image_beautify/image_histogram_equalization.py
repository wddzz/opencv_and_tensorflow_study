import cv2
import numpy as np


img0 = cv2.imread("H:\\Files\\image_process\\damimi.jpg",1)
# 灰度 直方图均衡化
# gray = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
# dst = cv2.equalizeHist(gray)
# 彩色 直方图均衡化
# (b,g,r) = cv2.split(img0)
# bdst = cv2.equalizeHist(b)
# gdst = cv2.equalizeHist(g)
# rdst = cv2.equalizeHist(r)
# dst = cv2.merge((bdst,gdst,rdst))#通道的合成
# YUV 均衡化
imgYUV = cv2.cvtColor(img0,cv2.COLOR_BGR2YCrCb)
channalYUV = cv2.split(imgYUV)
channalYUV[0] = cv2.equalizeHist(channalYUV[0])
channals = cv2.merge(channalYUV)
dst = cv2.cvtColor(channals,cv2.COLOR_YCrCb2BGR)
cv2.namedWindow("src",0)
cv2.resizeWindow("src",240,480)
cv2.imshow("src",img0)
cv2.namedWindow("dst",0)
cv2.resizeWindow("dst",240,480)
cv2.imshow("dst",dst)
cv2.waitKey(0)