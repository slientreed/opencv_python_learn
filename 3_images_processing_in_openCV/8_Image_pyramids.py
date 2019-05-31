'''
1. 图像金字塔（简单来说就是同一图像的不同分辨率的子图集合）

2. 分类：
高斯金字塔：顶部是通过将底部图像中的连续的行和列去除得到的。顶部图像中的每个像素值等于下一层图像中 5 个像素的高斯加权平均值，每次操作变成原来的四分之一。
拉普拉金字塔：由高斯金字塔得到，图像看起来就像边界图，其中很多像素都是 0。

3. 作用：
将降采样和平滑滤波结合在一起，对图像进行多尺度表示;可进行图形平滑融合。
'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.bmp',0)

# 由高分辨率大尺寸图像向上构建金字塔，尺寸变小，分辨率变低
lower_reso = cv2.pyrDown(img)
higher_reso2 = cv2.pyrUp(lower_reso)

# 拉普拉斯金字塔
tem1 = cv2.pyrDown(lower_reso)
tem2 = cv2.pyrUp(tem1)
lpalacian_reso = lower_reso - tem2  # 拉普拉斯金字塔计算方法

plt.subplot(221), plt.imshow(img,cmap='gray')
plt.title('Original')#, plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(lower_reso, cmap='gray')
plt.title('down')#, plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(higher_reso2, cmap='gray')
plt.title('up')#,plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(lpalacian_reso, cmap='gray')
plt.title('lapalcian')#,plt.xticks([]), plt.yticks([])

plt.show()
