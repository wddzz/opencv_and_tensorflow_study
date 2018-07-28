import cv2
import numpy as np
import time


img1 = cv2.imread("H:\\Files\\image_process\\damimi.jpg",3)
imgInfo = img1.shape
print(imgInfo)
height = imgInfo[0]
width = imgInfo[1]
for m in range(100,200):
    for n in range(100,300):
        if m%10 == 0 and n%10 == 0:
            for i in range(10):
                for j in range(10):
                    (b,g,r) = img1[m,n]
                    img1[i+m,j+n] = (b,g,r)
cv2.namedWindow("src",0)
cv2.resizeWindow("src",240,480)
cv2.imshow("src",img1)
cv2.waitKey(0)