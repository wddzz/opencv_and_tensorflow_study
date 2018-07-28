import cv2
import numpy as np


img = cv2.imread("damimi.jpg",1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# src 3 -> dst 3(左上角，左下角，右上角)
matSrc = np.float32([[0,0],[0,height-1],[width-1,0]])
matDsc = np.float32([[50,50],[300,height-200],[width-300,100]])
# 组合
matAffine = cv2.getAffineTransform(matSrc,matDsc)#mat 1 src 2 dst
dst = cv2.warpAffine(img,matAffine,(width,height))
cv2.namedWindow("newimg",0)
cv2.resizeWindow("newimg",240,480)
cv2.imshow("newimg",img)
cv2.imshow("dst",dst)
cv2.waitKey(0)
print(imgInfo)

# 图片的旋转
matRotate = cv2.getRotationMatrix2D((height*0.5,width*0.5),45,0.5)#1、旋转中心 2、旋转角度 3、缩放比例
dst = cv2.warpAffine(img,matRotate,(height,width))
cv2.imshow("newimg",dst)
cv2.waitKey(0)
