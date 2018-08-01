import cv2
import numpy as np


def ImageHist(image,type):
    color = (255,255,255)
    windowName = "Gray"
    if type == 31:
        color = (255,0,0)
        windowName = "B Hist"
    elif type == 32:
        color = (0,255,0)
        windowName = "G Hist"
    elif type == 33:
        color = (0,0,255)
        windowName = "R Hist"
    # 1、image 2、[0] 3、mask None 4、256 5、0-255
    hist = cv2.calcHist([image],[0],None,[256],[0.0,255.0])
    minV,maxV,minL,maxL = cv2.minMaxLoc(hist)
    histImage = np.zeros([256,256,3],np.uint8)
    for h in range(256):
        intenNormal = int(hist[h]*256/maxV)
        cv2.line(histImage,(h,256),(h,256-intenNormal),color)
    cv2.imshow(windowName, histImage)
    return histImage
img = cv2.imread("H:\\Files\\image_process\\anglebaby.jpg",1)
# cv2.imshow("dst",img)
channels = cv2.split(img)#RGB - R G B
for i in range(0,3):
    print(channels[i])
    ImageHist(channels[i],31+i)
cv2.waitKey(0)
# dst = np.zeros([256,256,3],np.uint8)
# cv2.line(dst,(0,100),(200,0),(0,0,255))
# cv2.imshow("dst",dst)
# cv2.waitKey(0)