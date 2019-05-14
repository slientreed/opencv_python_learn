import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('01.jpg')
rows,cols,w = img.shape

'''
# 扩展缩放

res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

height,width = img.shape[:2]
res = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

while(1):
    cv2.imshow('res',res)
    #cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xff == 27:
        break
cv2.destroyAllWindows()
'''

'''
# 平移
rows,cols,w = img.shape
#print(rows,cols)
M = np.float32([[1,0,200],[0,1,200]])
des = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',des)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
# 旋转
rows,cols, w = img.shape

# 旋转中心，旋转角，缩放因子
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,0.5)

# 第三个是图像尺寸中心
dst = cv2.warpAffine(img,M,(2*cols,2*rows))

while(1):
    cv2.imshow('img',dst)
    if cv2.waitKey(1) & 0xff == 27:
        break
cv2.destroyAllWindows()
'''

'''
# 仿射变换，在原图和变换后的图分别选三个点，保持三个点的平行关系不变
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
'''

# 透视变换，需要一个矩阵，变换后的直线还是直线
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
