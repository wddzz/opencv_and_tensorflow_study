import cv2
import numpy as np


img0 = cv2.imread("H:\\Files\\image_process\\damimi.jpg",1)
imgInfo = img0.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
dst = np.zeros((height,width,3),np.uint8)
for i in range(height-8):
    for j in range(width-8):
        array1 = np.zeros(8,np.uint8)
        print("aaaaaaaaaa")
        for m in range(8):
            for n in range(8):
                p1 = int(gray[i+m,j+n]/32)
                array1[p1] = array1[p1] + 1
        currentMax = array1[0]
        l = 0
        for k in range(0,8):
            if currentMax<array1[k]:
                currentMax = array1[k]
                l = k
        # 简化 均值
        for m in range(8):
            for n in range(8):
                if gray[i+m,j+n]>=(l*32) and gray[i+m,j+n]<=((l+1)*32):
                    (b,g,r) = img0[i+m,j+n]
        dst[i,j] = (b,g,r)
        print("bbbbbbbbbbbbbb")
cv2.namedWindow("dst",0)
cv2.resizeWindow("dst",240,480)
cv2.imshow("dst",img0)
cv2.waitKey(0)