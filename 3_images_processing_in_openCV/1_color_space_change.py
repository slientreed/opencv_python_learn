import cv2
import numpy as np


'''
# 可转换的颜色空间
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
'''

'''
# object tracking
cap = cv2.VideoCapture('/home/mark/Desktop/video_CAM7.avi')

while(1):
    _,frame = cap.read()

    # 转换颜色空间，GBR -> HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # 只留下blue
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
'''

'''
# 跟踪对应HSV的值
green = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
'''

# 