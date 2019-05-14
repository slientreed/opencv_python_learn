
import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)  # 绘制一个黑色图片画布

cv2.line(img, (0,0),(512,512),(255,0,0),5)
cv2.rectangle(img, (100,0), (510,128), (255,255,0),3)
cv2.circle(img, (447,100), 20, (0,255,0),5)
cv2.circle(img, (200,100), 20, (0,255,0),-1)
cv2.ellipse(img,(200,300),(80,50),0,0,180,255,-1)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 3,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('draw_line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


