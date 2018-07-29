import cv2
import numpy as np
import math


img0 = cv2.imread("H:\\Files\\image_process\\damimi.jpg",1)
imgInfo = img0.shape
height = imgInfo[0]
widht = imgInfo[1]
gray = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
dst = np.zeros((height,widht,1),np.uint8)
# newP = grayP0 - grayP1+150 加150增强图片的浮雕灰度等级，突出灰度的凸片及边缘特征
for i in range(0,height):
    for j in range(0,widht-1):
        grayP0 = int(gray[i,j])
        grayP1 = int(gray[i,j+1])
        newP = grayP0-grayP1+150
        if newP > 255:
            newP = 255
        if newP < 0:
            newP = 0
        dst[i,j] = newP
cv2.namedWindow("src",0)
cv2.resizeWindow("src",240,480)
cv2.imshow("src",dst)
cv2.waitKey(0)