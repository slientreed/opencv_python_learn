'''
1. 理解hough变换，如何检测直线
2. 学习函数：cv2.HoughLines()，cv2.HoughLinesP()
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('01.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize=3)

'''
# 参数1：二值化图像，参数2，3：精度，参数四：代表阈值
lines = cv2.HoughLines(edges,1,np.pi/180,200)
#print(lines)

for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('hough.jpg',img)
'''

# 优化版本hough变换
minLineLength = 100  # 比这个短的线段会被忽略
maxLineGap = 10  # 两条线段之间的最大间隔，小于此，会认为是同一条线段
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('hough_pro.jpg',img)

