'''
分水岭算法图像分割：
1. 基于掩膜思想
2. 函数：cv2.watershed()
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. 进行阈值分割，二值化
img = cv2.imread('01.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# 2. 使用形态学运算，去除图像中的白噪声：闭运算去除小空洞，腐蚀操作去除边缘像素

# 去除噪音
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
# 确定背景
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# 找到确定的前景图像，腐蚀
dist_transform = cv2.distanceTransform(opening,1,5)
ret,sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# 找到未知区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)



# 2. 找到背景和实体，进行创建标签。

# 打标签
ret,markers1 = cv2.connectedComponents(sure_fg)
# 加1，使得确定是背景的标签是1
markers = markers1+1
# 确保unknown区域标签是0
markers[unknown==255] = 0

# 标签完毕，实施分水岭算法。标签图像会被修改，边界区域标记变为-1
markers3 = cv2.watershed(img,markers)
img[markers3 == -1] = [255,0,0]


plt.subplot(221),plt.imshow(img,cmap='gray')
plt.title('Original Image'),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(thresh,cmap='gray')
plt.title('Thresh image'),plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(dist_transform,cmap='gray')
plt.title('Open Operation'),plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(markers3,cmap='gray')
plt.title('water seg'),plt.xticks([]),plt.yticks([])
plt.show()
