#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:10:21 2018

@author: pvictoratos
"""

import cv2
import numpy as np

img = cv2.imread('ostrich.jpg')
rows, cols = img.shape[:2]
image_center = (rows//2, cols//2)

px = img[100,100]
print(px)

b, g, r = cv2.split(img)

#Average Color
avgB = b.mean()
avgG = g.mean()
avgR = r.mean()

stdB = b.std()
stdG = g.std()
stdR = r.std()

btxt = str(avgB)
gtxt = str(avgG)
rtxt = str(avgR)

Avg = 'Avg: [ ' + btxt + ', ' + gtxt + ', ' + rtxt + ']'
Std = 'Std: [ ' + str(stdB) + ', ' + str(stdG) + ', ' + str(stdR) + ']'

font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img, Avg,(20, 65), font, 1,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img, Std, (20, 125), font, 1, (255,255,255),2,cv2.LINE_AA)


cv2.imshow("original", img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

img2 = cv2.merge((r,b,g))
cv2.imshow("Messed Up", img2)

def rotate_image(img, angle, scale):
    M = cv2.getRotationMatrix2D(image_center, angle, scale)
    rotated = cv2.warpAffine(r, M, (cols, rows))
    return rotated

rotatedRed = rotate_image(r, 45, 1.0)
img3 = cv2.merge((b, g, rotatedRed))
cv2.imshow("Rotated Red Channel", img3)



blues = np.zeros((rows, cols))
blues.fill(avgB)

greens = np.zeros((rows, cols))
greens.fill(avgG)

reds = np.zeros((rows, cols))
reds.fill(avgR)

img4 = cv2.merge((blues, greens, reds))
img4 = img4.astype(np.uint8)
cv2.imshow("Average Color", img4)

cv2.waitKey(0)