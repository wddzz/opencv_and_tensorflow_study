#imread
# 方法一 imread
import cv2
import numpy as np
import time
# img0 = cv2.imread("..\\damimi.jpg",0)
img1 = cv2.imread("..\\damimi.jpg",1)
# print(img0.shape)
# print(img1.shape)
# 方法二 cvtColor
# img = cv2.imread("H:\\Files\\image_process\\damimi.jpg",1)
# 在使用cv2.cvtColor时报错的处理，1：图片路径写完整路径；2：把图片和程序文件放在同一个文件夹下
# dst = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#颜色空间转换1、原参数(数据)2、转换模式
# 方法三
# RGB R=G=B = gray (R+G+B)/3
imgInfo= img1.shape
height = imgInfo[0]
width = imgInfo[1]
print(height,width)
dst = np.zeros((height,width,3),np.uint8)
# for i in range(height):
#     for j in range(width):
#         (b,g,r) = img1[i,j]
#         gray = (int(b)+int(g)+int(r))/3
#         dst[i,j] = np.uint8(gray)
# 方法四
now = time.time()
for i in range(height):
    for j in range(width):
        (b, g, r) = img1[i, j]
        b = int(b)
        g = int(g)
        r = int(r)
        # gray = r*0.2999 + g*0.587 + b*0.114
        #       优化：
        #       定点-》浮点  +、- 》*、/ >>
        # gray = (r+g*2+b)/4
        gray = (r+(g<<1)+b)>>2
        dst[i,j] = np.uint8(gray)

print(time.time()-now)
cv2.namedWindow("src",0)
cv2.resizeWindow("src",240,480)
cv2.imshow("src",dst)
# cv2.imshow("src",img0)
cv2.waitKey(0)