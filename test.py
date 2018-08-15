import matplotlib.pyplot as plt
import cv2
import numpy as np
drawing=False
mode="N" # N respect do nothing
ix,iy=-1,-1
rx,ry=-1,-1
lx,ly=-1,-1
r=-1
def SelectColorCallBack(x):
    pass


def SelectColor():
    r,g,b=0,0,0
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    return r,g,b
color=SelectColor()
def draw_circle(event,x,y,flags,param):
    global ix,iy,rx,ry,drawing,mode,r,lx,ly
    if event==cv2.EVENT_LBUTTONDOWN:
        print("left down")
        drawing=True
        ix,iy=x,y
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing==True:
            print("mode=", mode)
            if mode=="R"or mode== "r":
                print("rectangle")
                rx,ry=x,y
            elif mode=="C"or mode=="c":
                print("circle")
                r=np.sqrt(np.square(x-ix)+np.square(y-iy))
            elif mode=="L" or mode=="l":
                lx, ly = x, y
                print("line")

    elif event==cv2.EVENT_LBUTTONUP:
        if drawing==True:
            if mode=="R"or mode=="r":
                cv2.rectangle(img,(ix,iy),(rx,ry), SelectColor(),1)
            if mode=="C"or mode=="c":
                cv2.circle(img, (ix,iy), int(r), SelectColor(), 1)
            if mode=="L" or mode=="l":
                cv2.line(img,(ix,iy),(lx,ly), SelectColor(),1)
        drawing = False
img=cv2.imread(r'C:\Users\Administrator\Desktop\t01d53dd07ee8929638.jpg')
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, SelectColorCallBack)
cv2.createTrackbar('G', 'image', 0, 255, SelectColorCallBack)
cv2.createTrackbar('B', 'image', 0, 255, SelectColorCallBack)
cv2.setMouseCallback('image',draw_circle,color)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)
    if k==ord('R') or k==ord('r') :
        print("press m")
        mode="R"
    if k==ord('C') or k==ord('c') :
        print("press r")
        mode="C"
    if k == ord('L') or k == ord('l'):
        print("press l")
        mode="L"
    elif k==27:
        break
