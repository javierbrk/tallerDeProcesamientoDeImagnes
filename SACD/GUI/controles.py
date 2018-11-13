import cv2
import numpy as np

import imutils


def nothing(x):
    pass

# Create a black image, a window
#img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

cv2.namedWindow('trackbars')
cap = cv2.VideoCapture(0)

# create trackbars for color change
cv2.createTrackbar('R-low','trackbars',0,255,nothing)
cv2.createTrackbar('R-high','trackbars',0,255,nothing)

cv2.createTrackbar('G-low','trackbars',0,255,nothing)
cv2.createTrackbar('G-high','trackbars',0,255,nothing)

cv2.createTrackbar('B-low','trackbars',0,255,nothing)
cv2.createTrackbar('B-high','trackbars',0,255,nothing)


while(1):
    imagen = cv2.imread('6.jpg')
    img = imutils.resize(imagen, height=500)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    rl = cv2.getTrackbarPos('R-low','image')
    rh = cv2.getTrackbarPos('R-high','image')

    gl = cv2.getTrackbarPos('G-low','image')
    gh = cv2.getTrackbarPos('G-high','image')

    bl = cv2.getTrackbarPos('B-low','image')
    bh = cv2.getTrackbarPos('B-high','image')

    lower = np.array([rl,gl,bl])
    upper = np.array([rh,gh,bh])

    print(rl)

    img[:] = [bl,gl,rl]

    # Threshold the HSV image to get only certain colors
    mask = cv2.inRange(hsv, lower, upper)

    trackbars = np.zeros((300,512,3), np.uint8)


    res = cv2.bitwise_and(img,img, mask= mask)

    cv2.imshow('image',img)

    cv2.imshow('trackbars',trackbars)


cv2.destroyAllWindows()
