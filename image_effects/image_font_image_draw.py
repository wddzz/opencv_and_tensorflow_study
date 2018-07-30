import cv2
import numpy as np


img0 = cv2.imread("H:\\Files\\image_process\\damimi.jpg",1)
# 文字绘制
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img0,"this is fool",(100,300),font,1,(200,100,255),2,cv2.LINE_AA)
# 图片绘制
imgInfo = img0.shape
height = int(imgInfo[0]*0.1)
width = int(imgInfo[1]*0.1)
imgRize = cv2.resize(img0,(width,height))
for i in range(0,height):
    for j in range(0,width):
        img0[i+100,j+100] = imgRize[i,j]
cv2.namedWindow("dst",0)
cv2.resizeWindow("dst",240,480)
cv2.imshow("dst",img0)
cv2.waitKey(0)
