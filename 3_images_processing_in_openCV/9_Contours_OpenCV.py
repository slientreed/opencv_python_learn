'''
轮廓说明：
1. 为了更加准确，要使用二值化图像。在寻找轮廓之前，要进行阈值化处理、或者 Canny 边界检测
2. 查找轮廓的函数会修改原始图像
3. 在 OpenCV 中，查找轮廓就像在黑色背景中超白色物体
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.bmp')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,200,255,0)

# 三个参数：输入图像，轮廓检索模式，轮廓近似方法
# 返回值：图像，轮廓，轮廓的层析结构
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 参数：元素图像，轮廓，轮廓索引，轮廓颜色，厚度
img_draw = cv2.drawContours(thresh,contours,3,(0,255,0),3)

cnt = contours[0]

# 函数 cv2.moments() 会将计算得到的矩以一个字典的形式返回
M = cv2.moments(cnt)
#print("矩:",M)

# 计算对象的重心
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
#print("重心:",cx,cy)

# 计算轮廓的面积
area = cv2.contourArea(cnt)
#print("面积:",area)

# 计算轮廓周长
perimeter = cv2.arcLength(cnt,True)
#print("周长:", perimeter)

# 轮廓近似函数：cv2.approxPolyDP()，第二个参数叫epsilon，它是从原始轮廓到近似轮廓的最大距离。它是一个准确度参数
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
#print("近似轮廓",approx)

# 凸包：函数 cv2.convexHull() 可以用来检测一个曲线是否具有凸性缺陷，
hull = cv2.convexHull(cnt)
#print("凸包:",hull)

# 返回轮廓是不是凸包
k = cv2.isContourConvex(cnt)
#print(k)

# 边界矩形（不是最小面积矩形）
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)

# 旋转边界矩形：返回矩形左上角角点的坐标（x，y），矩形的宽和高（w，h），以及旋转角度。
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(img, [box], 0, (0,0,255),2)

# 最小外接圆
center,radius = cv2.minEnclosingCircle(cnt)
center_int = (int(center[0]), int(center[1]))
#print(center)
radius = int(radius)
img = cv2.circle(img,center_int,radius,(0,255,0),2)

# 椭圆拟合轮廓
#ellipse = cv2.fitEllipse(cnt)
#im = cv2.ellipse(im,ellipse,(0,255,0),2)

# 直线拟合轮廓
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)



## 轮廓性质
# 长宽比
x,y,w,h = cv2.boundingRect(cnt)
aspect_radio = float(w) / h
#print(aspect_radio)

# 面积比：轮廓面积和矩形面积比
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area) / rect_area
#print(extent)

# 轮廓面积和凸包面积比
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area) / hull_area
#print(solidity)

# 方向：对象的方向，返回长轴和短轴的长度
#(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)


## 掩膜和像素点：获得构成对象的所有像素点
# 获得像素点
mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#print(pixelpoints)

# 最大值，最小值，位置
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(imgray,mask=mask)
#print(min_val,max_val)
mean_val = cv2.mean(im,mask=mask)
print(mean_val)



# 轮廓的层次结构

# 明白cv2.findContours()参数的含义


'''
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
