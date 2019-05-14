import cv2
import numpy as np


'''
# 查看所有鼠标支持的事件，通过鼠标事件获得与鼠标对应的图片上的坐标
events=[i for i in dir(cv2) if 'EVENT'in i]  # dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表
print(events)

'''

'''
功能：右击可以画圆

# 回调函数：鼠标事件被引发，画一个实心圆
# 回调函数为draw_circle(),五个参数，参数由setMouseCallback()给
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 10, (255,0,0), -1)


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
# 1.设置回调函数：3个参数，第一个参数，表示将要操作的面板名，第二个参数是回调函数名，第三个是给回调函数的参数(如果有且较多，可以以列表传递)
cv2.setMouseCallback('image',draw_circle)


while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xff == 27:  # 按esc键退出
        break

cv2.destroyAllWindows()

'''

'''
# 功能：这一段是练习高级的鼠标画图功能

drawing = False
mode = True  # True画rectangle，False画circle，按下m键切换
ix,iy = -1,-1

# 定义回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy= x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                #pass
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xff
    if k == ord('m'):  # 切换模式为矩形还是圆形
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
'''


#功能： 这一段是使用滑动条做调色板

def nothing(x):
    pass

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
# createTrackbar()五个参数，最后一个是回调函数
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break


    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()