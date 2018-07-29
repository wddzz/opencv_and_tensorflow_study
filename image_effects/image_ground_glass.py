import cv2
import numpy as np
import random


img = cv2.imread("H:\\Files\\image_process\\damimi.jpg",1)
imgInfo = img.shape
height = imgInfo[0]
widht = imgInfo[1]
dst = np.zeros((height,widht,3),np.uint8)
num = 8
for i in range(height-num):
    for j in range(widht-num):
        index = int(random.random()*num)
        (b,g,r) = img[i+index,j+index]
        dst[i,j] = (b,g,r)
cv2.namedWindow("dst",0)
cv2.resizeWindow("dst",240,480)
cv2.imshow("dst",dst)
cv2.waitKey(0)