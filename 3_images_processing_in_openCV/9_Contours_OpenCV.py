'''
轮廓说明：
1. 为了更加准确，要使用二值化图像。在寻找轮廓之前，要进行阈值化处理、或者 Canny 边界检测
2. 查找轮廓的函数会修改原始图像
3. 在 OpenCV 中，查找轮廓就像在黑色背景中超白色物体
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt



