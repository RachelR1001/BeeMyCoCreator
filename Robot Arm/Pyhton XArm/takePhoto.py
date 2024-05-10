from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import sys
import time

#OpenCV Libraries
import cv2
import time
import numpy as np
import imutils
import urllib.request
from urllib.request import urlretrieve


def get_limits(color):
    c = np.uint8([[color]])  # bgr values that needed to be convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 20, 100, 100
    upperLimit = hsvC[0][0][0] + 20, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit

def take_img():
    # Save image
    img_url = 'http://192.168.137.162/saved-photo'  # img_url为图片链接
    file_name = 'testimg.jpeg'  # file_name为文件储存路径及文件名
    im_origin = cv2.imread('testimg.jpeg')
    h, w, c = -1, -1, -1
    ff = False

    while not ff:
        try:
            urlretrieve(img_url, file_name)  # 如果没有传入file_name，则urlretrieve会在Temp文件夹中生成一个临时文件。
            time.sleep(2)
            im_origin = cv2.imread('testimg.jpeg')

            # 得到图片大小
            h, w, c = im_origin.shape
            ff = True

        except:
            ff = False

    print(h)
    print(w)
    # Convert the image from rbg/bgr color space into hsv color space
    im = cv2.cvtColor(im_origin, cv2.COLOR_BGR2HSV)

    cv2.imshow('img_original', im_origin)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # Set up detecting Colors
    blue = [255, 0, 0]  # blue in BGR
    yellow = [0, 255, 255]  # yellow in BGR
    red = [0, 0, 255]  # red in BGR
    green = [0, 255, 0]  # green in BGR

    # Convert to limits
    blueLow, blueUp = (100, 40, 40), (130, 255, 255)
    yellowLow, yellowUp = get_limits(yellow)
    redLow, redUp = (170, 50, 50), (180, 255, 255)
    greenLow, greenUp = (50, 50, 50), (70, 255, 255)
    blackLow, blackUp = (5, 50, 50), (15, 255, 225)  # black

    """
    CONVERT TO HSV
    """
    # Convert the image from rbg/bgr color space into hsv color space
    im_hsv = cv2.cvtColor(im_origin, cv2.COLOR_BGR2HSV)

    # Get Masks
    blueMask = cv2.inRange(im_hsv, blueLow, blueUp)
    yellowMask = cv2.inRange(im_hsv, yellowLow, yellowUp)
    redMask = cv2.inRange(im_hsv, redLow, redUp)
    greenMask = cv2.inRange(im_hsv, greenLow, greenUp)
    blackMask = cv2.inRange(im_hsv, blackLow, blackUp)

    # Detect Four Points.
    redMask = cv2.medianBlur(redMask, 5)
    n1 = redMask.shape[0] / 16
    yellowMask = cv2.medianBlur(yellowMask, 5)
    n2 = yellowMask.shape[0] / 16
    blueMask = cv2.medianBlur(blueMask, 5)
    n3 = blueMask.shape[0] / 16
    greenMask = cv2.medianBlur(greenMask, 5)
    n4 = greenMask.shape[0] / 16
    blackMask = cv2.medianBlur(blackMask, 5)
    n5 = blackMask.shape[0] / 16

    cv2.waitKey()
    blueCircles = cv2.HoughCircles(blueMask, cv2.HOUGH_GRADIENT, 1, 50, n3, 300, 1, 10, 50)
    yellowCircles = cv2.HoughCircles(yellowMask, cv2.HOUGH_GRADIENT, 1, 50, n2, 100, 1, 10, 50)
    redCircles = cv2.HoughCircles(redMask, cv2.HOUGH_GRADIENT, 1, 50, n1, 300, 1, 10, 50)
    greenCircles = cv2.HoughCircles(greenMask, cv2.HOUGH_GRADIENT, 1, 50, n4, 200, 1, 10, 50)
    blackCircles = cv2.HoughCircles(blackMask, cv2.HOUGH_GRADIENT, 1, 50, n5, 200, 1, 10, 30)
    blackCircles = np.uint16(np.around(blackCircles))
    blueCircles = np.uint16(np.around(blueCircles))
    yellowCircles = np.uint16(np.around(yellowCircles))
    redCircles = np.uint16(np.around(redCircles))
    greenCircles = np.uint16(np.around(greenCircles))

    b = blueCircles[0][0]
    print(b)
    y = yellowCircles[0][0]
    print(y)
    r = redCircles[0][0]
    print(r)
    g = greenCircles[0][0]
    print(g)
    black = blackCircles[0][0]
    print(black)

    bx = b[0]
    by = 1200 - b[1]

    yx = y[0]
    yy = 1200 - y[1]

    rx = r[0]
    ry = 1200 - r[1]

    gx = g[0]
    gy = 1200 - g[1]

    originX = black[0]
    originY = 1200 - black[1]

    print("re")
    print([rx, ry])  # red point will be the "origin"
    print("blue")
    print([bx, by])
    print("ye")
    print([yx, yy])
    print("gre")
    print([gx, gy])


    list1 = [r, b, y, g, black]
    for i in list1:
        i = np.array(i, dtype=np.float64)
        cv2.circle(im_origin, (int(i[0]), int(i[1])), int(i[2]), (0, 0, 255), 2)
        cv2.circle(im_origin, (int(i[0]), int(i[1])), 1, (255, 0, 0), 2)
        imS = cv2.resize(im_origin, (800, 600))
        cv2.imshow('im', imS)

        cv2.waitKey()
        print("position")
        print(i[0] - originX)
        print((1200 - i[1]) - originY)
    cv2.destroyAllWindows()

    X=140
    Y=280

    origin_list = [(X+ry/5,Y-rx/5),(X+by / 5,Y- bx / 5),(X + yy / 5,Y- yx / 5),(X+ gy / 5,Y- gx / 5)]

    return origin_list



# origin arm X=140 Y = 280
