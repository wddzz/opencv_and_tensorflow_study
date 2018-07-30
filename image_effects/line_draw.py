import cv2
import numpy as np


newImageInfo = (500,500,3)
dst = np.zeros(newImageInfo,np.uint8)
# line
# 绘制线段1、dst 2、begin 3、end 4、color
# cv2.line(dst,(100,100),(400,400),(0,0,255))
# 5、line w
# cv2.line(dst,(100,200),(400,200),(0,255,255),20)
# 6、line type
# cv2.line(dst,(100,300),(400,300),(0,255,0),20,cv2.LINE_AA)
#调用API绘制矩形
# 1、原始数据 2、左上角 3、右下角 4、颜色 5、是否填充：小于0表示填充，大于0表示线条的宽度
# cv2.rectangle(dst,(50,100),(200,300),(255,0,0),5)
#调用API绘制圆形
# 1、原始数据 2、圆心 3、半径 4、颜色 5、是否填充：小于0表示填充，大于0表示线条的宽度
# cv2.circle(dst,(250,250),(50),(0,255,0),2)
# 椭圆形的绘制
# 1、原始数据 2、圆心 3、长轴 短轴 4、起始角度 5、偏转角度 6、终止角度 7、颜色 8、是否填充：小于0表示填充，大于0表示线条的宽度
# cv2.ellipse(dst,(256,256),(150,100),0,360,0,(255,255,0),-1)
# 任意多边形的绘制
points = np.array([[150,50],[140,140],[200,170],[250,250],[150,50]],np.int32)
print(points.shape)
points = points.reshape((-1,1,2))
print(points.shape)
cv2.polylines(dst,[points],True,(0,255,255))
cv2.imshow("dst",dst)
cv2.waitKey(0)
