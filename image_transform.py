import cv2
import numpy as np


img = cv2.imread("damimi.jpg",1)#1表示读取的是彩色图片
imgInfo = img.shape
print(imgInfo)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]
dstHeight = int(height*0.5)
dstWidth = int(width*0.5)
# 最近临域插值#双线性插值#像素关系重采样#立方插值
dst = cv2.resize(img,(dstWidth,dstHeight))
cv2.imshow("image",dst)
cv2.waitKey(0)
print(dst.shape)

# 源码的形式实现图片的缩放
dstImage = np.zeros((dstHeight,dstWidth,3),np.uint8)
for i in range(0,dstHeight):
    for j in range(0,dstWidth):
        iNew = int(i*(height*1.0/dstHeight))
        jNew = int(j*(width*1.0/dstWidth))
        dstImage[i,j] = img[iNew,jNew]
cv2.imshow("dst",dstImage)
cv2.waitKey(0)

# 图片剪切
# 100 -》200 x
# 100 -》300 y
dst = img[100:200,100:300]
cv2.imshow('image',dst)
cv2.waitKey(0)
