
'''
1. 使用OpenCV对图像进行傅里叶变换，Numpy中FFT函数
2. 函数有：cv2.dft()，cv2.idft() 等
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.bmp',0)

'''
# 对信号进行频率转换，输出一个复杂数组；
f = np.fft.fft2(img)
# 把频率为0的部分沿两个方向平移，从输出图像左上角移到图像中心
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))  # 构建振幅图


plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Input Image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum,cmap='gray')
plt.title('Magnitude Spectum'),plt.xticks([]),plt.yticks([])
plt.show()

# 进行频域变换
rows, cols = img.shape
# print(rows,cols)
crow,ccol = int(rows / 2), int(cols / 2)
print(crow,ccol)
# 取一个60*60窗口对图像进行掩膜操作去除低频分量
fshift[crow-30:crow+30,ccol-30:ccol+30] = 0
# 逆平移操作，使得直流分量回到左上角
f_ishift = np.fft.ifftshift(fshift)
# fft逆变换
img_back = np.fft.fft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img,cmap='gray')
plt.title('Input Image'),plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

plt.show()
'''


# 2.使用OpenCV实现傅里叶变换
dft = cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

'''
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
'''

# 3. DFT逆变换，做低通滤波去除高频，对图像进行模糊操作。
#    构建一个掩模，与低频区域对应的地方设置为 1, 与高频区域对应的地方设置为0。

rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)

# 构造一个掩膜，中心区域（低频）设置为0，其他（高频）设置为1
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# 使用掩膜，DFT逆变换
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


