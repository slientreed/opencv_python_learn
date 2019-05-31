
'''
简介：canny边缘检测算法由很多步骤构成的算法：
1. 去噪：高斯滤波器
2. 计算梯度：Sobel计算水平和竖直梯度
3. 非极大值抑制：去除非边界的点
4. 滞后阈值：确定真正的边界

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.bmp',0)

# 参数分别是：输入图像，minval，maxval,梯度sobel卷积核大小，L2grade求梯度大小方程
edges = cv2.Canny(img,150,160)

plt.subplot(121), plt.imshow(img,cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Sobel Edge'), plt.xticks([]), plt.yticks([])

plt.show()

