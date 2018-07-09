import cv2

# 1、文件的读取；2、封装格式解析；3、数据解码；4、数据加载
img = cv2.imread("damimi.jpg", 1)#图片路径，1：表示彩色图像（默认）
# cv2.imshow("image", img)#窗体名称，展示的内容
# # JPG，PNG 1、文件头；2、文件数据(原始数据)  1.4M-->130k
# cv2.waitKey(0)#程序暂停
#
# # 图片的写入
# cv2.imwrite("damimi02.jpg", img)
#
# # 不同图片质量保存
# cv2.imwrite("damimi_yasuo.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 0])#1M-100k-10k;取值范围0-100，有损压缩,取值越小，损失越严重
# # jpg压缩比0-100，数字越小，压缩比越高；png压缩比0-9，数字越小，压缩比越低
# cv2.imwrite("damimi_yasuo.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

# 像素的读取和写入,灰度图只有一个值
(b,g,r) = img[100,100]
print(b,g,r)
# 设置（10，100）-（110,100）为蓝色
for i in range(1, 100):
    img[10+i,100] = (255, 0, 0)
cv2.imshow("image",img)
cv2.waitKey(0)#1000ms