import cv2
import os
from matplotlib import pyplot as plt

path = os.getcwd()
img = cv2.imread('01.jpg',0)

'''
cv2.imshow('image01',img)
k = cv2.waitKey(0)  # 等待键盘按键按下

if k == 27:   # 按下esc键盘退出
    cv2.destroyAllWindows()
elif k == ord('s'): # s键按下保存并退出, ord()返回字符串对应的ascll值
    cv2.imwrite('image01.png',img)
    print("图片已经保存！")
    cv2.destroyAllWindows()
'''

# 使用matplotlib显示图片
# 看一下怎么加载彩色，opencv读入BGR格式，Matplotib是RGB格式，有些区别？
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]),plt.yticks([])  # hide x,y tric value
plt.show()