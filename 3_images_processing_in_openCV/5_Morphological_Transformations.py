import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('01.jpg')


kernel = np.ones((5,5),np.uint8)

# 1. 腐蚀前景物体边界，卷积核沿着图像滑动，如果与卷积核对应的原图像的所有像素值都是 1，那么中心元素就保持原来的像素值，否则就变为零。
# 可以用来分割物体
erosion = cv2.erode(img,kernel,iterations=1)

# 2. 腐蚀，相反，与卷积核对应的原图像的像素值中只要有一个是 1，中心元素的像素值就是 1。所以这个操作会增加图像中的白色区域（前景）
# 可以用来连接两个物体
dilation = cv2.dilate(img,kernel,iterations=1)


# 3,开运算：先腐蚀再膨胀，用于去除噪声
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 4.闭运算：先膨胀，在腐蚀。去除前景中的物体
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 5.形态学梯度：图像膨胀和腐蚀的差别,前景的轮廓
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT,kernel)

# 6.礼帽:原始图像和开运算之后的差
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 7.黑帽： 原始图像和闭运算之后的差
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT,kernel)




plt.subplot(121),plt.imshow(img),plt.title('Origional')
plt.subplot(122),plt.imshow(blackhat),plt.title('erosion')
plt.show()


'''
[参考]()
'''