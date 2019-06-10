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

# 均衡化计算
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())

cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]
plt.hist(img2.flatten(),256,[0,256],color='r')
plt.show()


# OpenCV里的直方图函数：cv2.equalizeHist()
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imwrite('res.png',res)
plt.imshow(res, cmap='gray', interpolation='bicubic')
plt.xticks([]),plt.yticks([])  # hide x,y tric value
plt.show()

# 自适应直方图均衡化CLAHE，把图像分成很多小块，然后对每个小块进行直方图均衡化
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imwrite('clahe_2.jpg',cl1)
plt.imshow(cl1)
plt.show()




# 4. 2D直方图
# 对于彩色图像的直方图通常情况下我们需要考虑每个的颜色（Hue）和饱和度（Saturation）。根据这两个特征绘制 2D 直方图

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# H 通道为 180，S 通道为 256；H 的取值范围在 0 到 180，S 的取值范围在 0 到 256
hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

plt.imshow(hist,interpolation='nearest')  # inter插值参数为nearest
plt.show()
#print(hist)
'''



# 5. 直方图反向投影：用来做图像分割，或者在图像中找寻我们感兴趣的部分
# 使用颜色直方图；
# 接着我们再把这个颜色直方图投影到输入图像中寻找我们的目标，也就是找到输入图像中的每一个像素点的像素值在直方图中对应的概率；
# 最后设置适当的阈值对概率图像进行二值化

#roi is the object or region of object we need to find
roi = cv2.imread('image.bmp')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

#target is the image we search in
target = cv2.imread('01.jpg')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

M = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
I = cv2.calcHist([hsvt],[0,1],None,[180,256],[0,180,0,256])

# 与内核进行卷积,得出每个像素属于目标像素的概率
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
B=cv2.filter2D(I,-1,disc)
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

#现在输出图像中灰度值最大的地方就是我们要查找的目标的位置了,使用阈值进行阈值化
ret,thresh = cv2.threshold(B,50,255,0)
plt.imshow(thresh)
plt.show()

