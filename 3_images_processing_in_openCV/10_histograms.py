'''
目标：
1. 计算直方图，且绘制直方图
2. 将要学习的函数有：cv2.calcHist()，np.histogram()

直方图：灰度图像，对图像的灰度有个整体的了解，x轴是灰度值，y轴是灰度值的数目。
       通过直方图我们可以对图像的对比度，亮度，灰度分布等有一个直观的认识。
'''





import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.bmp')

'''
#1.返回一个一维直方图数组
#hist = cv2.calcHist([img],[0],None,[256],[0,256])
#print(hist)

color = ('b','g','r')
for i,col in enumerate(color):
    histre = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histre,color=col)
    plt.xlim([0,256])
    plt.show()
'''

'''
# 2.使用掩模
# 统计图像某个局部区域的直方图只需要构建一副掩模图像。将要统计的部分设置成白色，其余部分为黑色，把掩膜图像传给函数。

# create a mask
mask = np.zeros(img.shape[:2],np.uint8)
mask[100:300,100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask=mask)

# calculate histogram with mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.imshow(mask,'gray')
plt.subplot(223),plt.imshow(masked_img,'gray')
plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()
'''

# 3. 直方图均衡化
# 把像素直方图横向拉伸，使得灰度值更加均衡

hist,bins = np.histogram(img.flatten(),256,[0,256])
# 计算累计分布
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()
plt.plot(cdf_normalized,color='b')
plt.hist(img.flatten(),256,[0,256],color='r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'),loc='upper left')
plt.show()
