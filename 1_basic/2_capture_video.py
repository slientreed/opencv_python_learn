
'''
1. 这个是官网的代码，但是不知道为什么有问题，Ubuntu下无法打开内置摄像头

'''


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    print(ret)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitkey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()