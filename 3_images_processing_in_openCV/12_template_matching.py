'''
模板匹配：
1. 使用模板在一幅图像中查找目标：
2. 函数：cv2.matchTemplate()：用模板图像在输入图像（大图）上滑动，并在每一个位置对模板图像和与其对应的输入图像的子区域进行比较；
                            OpenCV 提供了几种不同的比较方法（细节请看文档）。返回的结果是一个灰度图像，每一个像素值表示了此区域与模板的匹配程度；

         cv2.minMaxLoc()：找到返回灰度图像结果的最小值和最大值位置。
                          第一个值为矩形左上角的点（位置），（w，h）为 moban 模板矩形的宽和高。
                          这个矩形就是找到的模板区域了
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.bmp',0)
img2 = img.copy()
template = cv2.imread('template.jpg',0)
w,h = template.shape[::-1]   # 翻转template的尺寸
print(w,h)
# print(template.shape)

# 6种对比方法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # 使用模板在目标上匹配
    res = cv2.matchTemplate(img,template,method)
    # 返回灰度结果的最大最小值
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0]+w,top_left[1]+h)      # 右下角坐标
    cv2.rectangle(img,top_left,bottom_right,255,2)

    plt.subplot(131),plt.imshow(res,cmap='gray')
    plt.title('Match Result'),plt.xticks([]),plt.yticks([])
    plt.subplot(132),plt.imshow(img,cmap='gray')
    plt.title('Detected Point'),plt.xticks([]),plt.yticks([])
    plt.subplot(133),plt.imshow(template,cmap='gray')
    plt.title('Template Image'),plt.xticks([]),plt.yticks([])
    plt.suptitle(meth)

    plt.show()

