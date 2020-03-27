import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
cv2.namedWindow("Output", cv2.WINDOW_NORMAL)

img = cv2.imread('3a55023a-a01b-493a-aa87-2a6f98c47066.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
cnt, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

maximum = 0
index = -1
for j,i in enumerate(cnt):
    area = cv2.contourArea(i)
    if area > maximum:
        maximum = area
        index = j

mask = np.zeros_like(imgray) # Create mask where white is what we want, black otherwise
cv2.drawContours(mask, cnt, index, 255, -1) # Draw filled contour in mask
out = np.zeros_like(img) # Extract out the object and place into output image
out[mask == 255] = img[mask == 255]

x = np.zeros(4, dtype=int)
y= np.zeros(4, dtype=int)

(a, b) = np.where(mask == 255)
arr = a-b
ind = np.argmin(arr)
y[3], x[3] = a[ind], b[ind]

ind = np.argmax(arr)
y[1], x[1] = a[ind], b[ind]

arr = a+b
ind = np.argmin(arr)
y[0], x[0] = a[ind], b[ind]

ind = np.argmax(arr)
y[2], x[2] = a[ind], b[ind]

# Show the output image
cv2.imshow('Output', img)


def distance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return int(dist)


size_x = max(distance(x[0],y[0],x[3],y[3]),distance(x[1],y[1],x[2],y[2]))
size_y = max(distance(x[0],y[0],x[1],y[1]),distance(x[2],y[2],x[3],y[3]))

rows,cols,ch = img.shape
pts1 = np.float32([[x[0],y[0]],[x[3],y[3]],[x[1],y[1]],[x[2],y[2]]])
pts2 = np.float32([[0,0],[size_x,0],[0,size_y],[size_x,size_y]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(size_x,size_y))
cv2.imwrite('docu.jpg', dst)

plt.imshow(dst)
plt.show()
cv2.waitKey(0)
