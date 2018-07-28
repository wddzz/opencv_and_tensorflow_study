import cv2
import numpy as np


img = cv2.imread("damimi.jpg",1)
cv2.imshow("src",img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# 矩阵的拆分
matShift = np.float32([[1,0,100],[0,1,200]])
dst = cv2.warpAffine(img,matShift,(height,width))
cv2.imshow("dst",dst)
cv2.waitKey(0)

#图片位移
dstt = np.zeros(img.shape,np.uint8)
for i in range(0,height):
    for j in range(0,width):
        dstt[i,j+100] = img[i,j]
cv2.imshow("image",dstt)
cv2.waitKey(0)
