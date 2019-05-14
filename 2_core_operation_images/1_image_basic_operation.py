import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit
import time

img = cv2.imread('01.jpg')
px = img[100,100]  # 根据坐标获取图片像素值,返回三维，BGR
#print(px)

blue = img[100,100,0]  # 返回B的值
#print(blue)

'''
# 使用numpy修改，获得像素点的值
print(img.item(10,10,1))
img.itemset((10,10,1),100)
print(img.item(10,10,1))
'''

'''
# 获取图像属性
print(img.shape)
print(img.size,img.dtype)  # 像素点数目，图像数据类型
'''

'''
# 图像ROI
ball=img[280:340,330:390]
img[273:333,100:160]=ball   # 把ball区域的图片拷贝到其他区域，实现对ball复制د
img=cv2.imshow('test', img)
cv2.waitKey(0)
'''

'''
# 拆分及合并通道
b,g,r = cv2.split(img)
img[:,:,2] = 0
cv2.imshow('image',img)
cv2.waitKey(0)
'''

'''
# 为图像填充，扩边
BLUE = [255,0,0]
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
'''

'''
# 性能检测
e1 = cv2.getTickCount()
for i in range (5,49,2):
    img1 = cv2.medianBlur(img,1)
e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()
print(t)
'''

cv2.useOptimized()
