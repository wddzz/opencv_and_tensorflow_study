import cv2
import numpy as np
import math


img0 = cv2.imread("H:\\Files\\image_process\\damimi.jpg",1)
imgInfo = img0.shape
height = imgInfo[0]
widht = imgInfo[1]
# grb -> RGB new "蓝色"
# b=b*1.5
# g=g*1.3
dst = np.zeros((height,widht,3),np.uint8)
for i in range(0,height):
    for j in range(0,widht):
        (b,g,r) = img0[i,j]
        b = b*1.5
        g = g*1.3
        if b>255:
            b=255
        if g>255:
            g=255
        dst[i,j] = (b,g,r)
cv2.namedWindow("src",0)
cv2.resizeWindow("src",240,480)
cv2.imshow("src",dst)
cv2.waitKey(0)