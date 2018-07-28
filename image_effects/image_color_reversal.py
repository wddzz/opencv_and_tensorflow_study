import cv2
import numpy as np
import time


img1 = cv2.imread("H:\\Files\\image_process\\damimi.jpg",1)
imgInfo = img1.shape
height = imgInfo[0]
width = imgInfo[1]
# 灰度图片颜色翻转
# img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# dst = np.zeros((height,width,1),np.uint8)
# 彩色图片颜色翻转
dst = np.zeros((height,width,3),np.uint8)
for i in range(height):
    for j in range(width):
        # 灰度图片颜色翻转
        # gray = img[i,j]
        # dst[i,j] = 255-gray

        #彩色图片颜色翻转
        (b,g,r) = img1[i,j]
        dst[i,j] = (255-b,255-g,255-r)
cv2.namedWindow("src",0)
cv2.resizeWindow("src",240,480)
cv2.imshow("src",dst)
cv2.waitKey(0)