import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('download.png')


# 平均滤波 ： 求某个像素周围像素和核的平均值
kernel = np.ones((5,5),np.float32) / 5
#blur = cv2.filter2D(img, -1, kernel)


# 图像模糊：1.平均
#blur = cv2.blur(img,(5,5))

# 2.高斯滤波：把卷积核换成高斯核
#blur = cv2.GaussianBlur(img, (5,5), 0)

# 3. 中值滤波： 用与卷积框对应像素的中值来替代中心像素的值
#blur = cv2.medianBlur(img,5)

# 4.双边滤波  ： 双边滤波在同时使用空间高斯权重和灰度值相似性高斯权重，
blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(blur),plt.title('Averageing')
plt.xticks([]),plt.yticks([])
plt.show()


