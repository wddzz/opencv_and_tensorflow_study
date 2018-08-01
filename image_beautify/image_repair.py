import cv2
import numpy as np


img = cv2.imread("bad.jpg",1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
img0 = np.zeros([height,width,1],np.uint8)
for i in range(200,300):
    img0[200,i] = 255
    img0[200+1,i] = 255
    img0[200+2,i] = 255
for i in range(150,250):
    img0[i,250] = 255
    img0[i,250+1] = 255
    img0[i,250+2] = 255

# cv2.imwrite("bad.jpg",img0)
dst = cv2.inpaint(img,img0,3,cv2.INPAINT_TELEA)
cv2.namedWindow("dst",0)
cv2.resizeWindow("dst",480,960)
cv2.imshow("img0",img0)
cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey(0)



# img = np.zeros([255,100,3],np.uint8)
# print(img.shape)
# cv2.line(img,(0,100),(200,0),(0,0,255))
# cv2.imshow("img",img)
# cv2.waitKey(0)