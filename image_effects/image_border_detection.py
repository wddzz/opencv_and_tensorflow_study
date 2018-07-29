# import cv2
# import numpy as np
#
# img0 = cv2.imread("H:\\Files\\image_process\\damimi.jpg",1)
# imgInfo = img0.shape
# height = imgInfo[0]
# widht = imgInfo[1]
# canny 1、gray 2、高斯 3、canny
# gray = cv2.cvtColor(img0,cv2.COLOR_RGB2GRAY)
# imgG = cv2.GaussianBlur(gray,(3,3),0)
# dst = cv2.Canny(img0,50,50)#1、data 2、th 图片卷积--》》th
# cv2.namedWindow("src",0)
# cv2.resizeWindow("src",240,480)
# cv2.imshow("src",dst)
# cv2.waitKey(0)


#源码实现边缘检测
import cv2
import numpy as np
import math


img0 = cv2.imread("H:\\Files\\image_process\\damimi.jpg",1)
imgInfo = img0.shape
height = imgInfo[0]
widht = imgInfo[1]
# sobel 1、算子模板 2、图片卷积 3、阀值判决
# [1 2 1                    [1 0 -1
#  0 0 0                     2 0 -2
#  -1 -2 -1]                 1 0 -1]

# [1 2 3 4] [a b c d] a*1+b*2+c*3+d*4 = dst
# sqrt(a*a+b*b) = f>th
gray = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
dst = np.zeros((height,widht,1),np.uint8)
for i in range(0,height-2):
    for j in range(0,widht-2):
        gy = gray[i,j]*1+gray[i,j+1]*2+gray[i,j+2]*1-gray[i+2,j]*1-gray[i+2,j+1]*2-gray[i+2,j+2]*1
        gx = gray[i,j]*1+gray[i+1,j]*2+gray[i+2,j]*1-gray[i,j+2]*1-gray[i+1,j+1]*2-gray[i+2,j+2]*1
        grad = math.sqrt(gx*gx+gy*gy)
        if grad >50:
            dst[i,j] = 255
        else:
            dst[i,j] = 0
cv2.namedWindow("src",0)
cv2.resizeWindow("src",240,480)
cv2.imshow("src",dst)
cv2.waitKey(0)

