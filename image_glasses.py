import cv2
import numpy as np

# cv2.HoughLinesP

img = cv2.imread("damimi.jpg",1)
imgInfo = img.shape
print(imgInfo)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]
data = (height*2,width,mode)
dstImg = np.zeros(data,np.uint8)
for i in range(0,height):
    for j in range(0,width):
        dstImg[i,j] = img[i,j]
        dstImg[height*2-i-1,j] = img[i,j]#减去1，imgInfo=(2560, 1440, 3),0~2560
for k in range(0,width):
    dstImg[height,k] = (0,0,255)
cv2.namedWindow("enhanced",0)
cv2.resizeWindow("enhanced", 240, 480)
cv2.imshow("enhanced",dstImg)
cv2.waitKey(0)

# cv2.imshow("src",img)

# 图片的缩放
# [[A1 A2 B1],[A3 A4 B2]]
# [[A1 A2],[A3 A4]]  [[B1],[B2]]
# newX = A1*x + A2*y + B1
# newY = A3*x + A4*y + B2
# x->x*0.5 y->y*0.5
# newX = 0.5*x
matScale = np.float32([[0.5,0,0],[0,0.5,0]])
dst = cv2.warpAffine(img,matScale,(int(width/2),int(height/2)))
cv2.imshow('dst',dst)
cv2.waitKey(0)

