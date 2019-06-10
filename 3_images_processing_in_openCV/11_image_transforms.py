
'''
1. 使用OpenCV对图像进行傅里叶变换，Numpy中FFT函数
2. 函数有：cv2.dft()，cv2.idft() 等
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.bmp')
