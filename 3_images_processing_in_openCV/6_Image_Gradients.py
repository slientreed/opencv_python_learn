'''
图像梯度：计算图像像素某个领域的灰度变化，类似导数，图像梯度变化较大时，可能是边缘
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.bmp',0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
plt.title('Origional'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

