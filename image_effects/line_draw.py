import cv2
import numpy as np


newImageInfo = (500,500,3)
dst = np.zeros(newImageInfo,np.uint8)
# line
# 绘制线段1、dst 2、begin 3、end 4、color
cv2.line(dst,(100,100),(400,400),(0,0,255))
# 5、line w
cv2.line(dst,(100,200),(400,200),(0,255,255),20)
# 6、line type
cv2.line(dst,(100,300),(400,300),(0,255,0),20,cv2.LINE_AA)


cv2.imshow("dst",dst)
cv2.waitKey(0)