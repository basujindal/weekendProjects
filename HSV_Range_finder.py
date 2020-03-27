import cv2
import numpy as np


def nothing(x):
  pass

cv2.namedWindow('Trackbar')
cv2.createTrackbar("U_H", "Trackbar",255,180,nothing)
cv2.createTrackbar("U_S", "Trackbar",255,255,nothing)
cv2.createTrackbar("U_V", "Trackbar",255,255,nothing)

cv2.createTrackbar("L_H", "Trackbar",0,180,nothing)
cv2.createTrackbar("L_S", "Trackbar",0,255,nothing)
cv2.createTrackbar("L_V", "Trackbar",0,255,nothing)

img = cv2.imread('TL_G.png', 1)
img2 = cv2.imread('TL_Y.png', 1)
img3 = cv2.imread('TL_red.png', 1)
img = cv2.resize(img, (200, 500))
img3 = cv2.resize(img3, (200, 500))
img2 = cv2.resize(img2, (200, 500))
img4 = img + img2 + img3


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
hsv4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)


while 1:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    Uh = cv2.getTrackbarPos('U_H','Trackbar')
    Us = cv2.getTrackbarPos('U_S','Trackbar')
    Uv = cv2.getTrackbarPos('U_V','Trackbar')
    Lh = cv2.getTrackbarPos('L_H','Trackbar')
    Ls = cv2.getTrackbarPos('L_S','Trackbar')
    Lv = cv2.getTrackbarPos('L_V','Trackbar')
    print(Uh,Us,Uv,Lh,Ls,Lv)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low_yellow = np.array([Lh, Ls, Lv])
    up_yellow = np.array([Uh, Us, Uv])
    mask = cv2.inRange(hsv, low_yellow, up_yellow)
    mask2 = cv2.inRange(hsv2,low_yellow,up_yellow)
    mask4 = cv2.inRange(hsv4,low_yellow,up_yellow)
    res = cv2.bitwise_and(img,img,mask=mask)
    res2 = cv2.bitwise_and(img2,img2,mask=mask2)
    res4 = cv2.bitwise_and(img4,img4,mask=mask4)
    cv2.imshow('image',res)
    cv2.imshow('img',mask)
    cv2.imshow('image2',res2)
    cv2.imshow('img2',mask2)
    cv2.imshow('image4',res4)
    cv2.imshow('img4',mask4)




cv2.waitKey(0)
cv2.destroyAllWindows()