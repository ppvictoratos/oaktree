# -*- coding: utf-8 -*-
"""
Fruit Counter

This program looks at an input image and counts the number of apples, bananas 
and oranges. It does so by...
"""
import cv2
import numpy as np

fruitImg = cv2.imread('mixed_fruit2.tiff')
img = fruitImg.astype(np.float)
img *= 1.5
img = np.clip(img, 0, 255)
img = img.astype(np.uint8)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(hsv)
R, G, B = cv2.split(img)

#Thresholding for Apple-Like Hues
hRedLow = 80
hRedHi = 200
sRedLow = 173
sRedHi = 241

ret, redH = cv2.threshold(H, hRedLow, 255, cv2.THRESH_BINARY)
ret, redH2 = cv2.threshold(H, hRedHi, 255, cv2.THRESH_BINARY_INV)
redHue = cv2.bitwise_and(redH, redH2)

ret, redS = cv2.threshold(S, sRedLow, 255, cv2.THRESH_BINARY)
ret, redS2 = cv2.threshold(S, sRedHi, 255, cv2.THRESH_BINARY_INV)
redSat = cv2.bitwise_and(redS, redS2)

redMask = cv2.bitwise_and(redHue, redSat)

strel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
opened = cv2.morphologyEx(redHue, cv2.MORPH_OPEN, strel)
strel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (27, 27))
RedMask = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, strel2)

#cv2.imshow("Brightened", img)
#cv2.imshow("Red Hue", redHue)
#cv2.imshow("Red Saturation", redSat)
#cv2.imshow("Red Mask", RedMask)

#Find Red Contours
_, contours, _ = cv2.findContours(RedMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
show_apples = fruitImg.copy()

counter = 0

for c in contours:
    counter = counter + 1    
    x, y, w, h = cv2.boundingRect(c)
    cv2.drawContours(show_apples, [c], -1, (0, 0, 255), 3)

counter = str (counter)
messageRed = "I found " + counter + " apples"
textApple = show_apples.copy()
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(textApple, messageRed, (15, 15), font, 0.5,(0, 0, 255), 2)

cv2.imshow("Apple Contours", textApple)

#=====================================================
#Thresholding for Banana-Like Hues
hYelLow = 23
hYelHi = 45
sYelLow = 160
sYelHi = 200

ret, yelH = cv2.threshold(H, hYelLow, 255, cv2.THRESH_BINARY)
ret, yelH2 = cv2.threshold(H, hYelHi, 255, cv2.THRESH_BINARY_INV)
yelHue = cv2.bitwise_and(yelH, yelH2)

ret, yelS = cv2.threshold(S, sYelLow, 255, cv2.THRESH_BINARY)
ret, yelS2 = cv2.threshold(S, sYelHi, 255, cv2.THRESH_BINARY_INV)
yelSat = cv2.bitwise_and(yelS, yelS2)

yelMask = cv2.bitwise_and(yelHue, yelSat)

strelY = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
openedY = cv2.morphologyEx(yelMask, cv2.MORPH_OPEN, strelY)
strelY2 = cv2.getStructuringElement(cv2.MORPH_RECT, (57, 57))
yelMorph = cv2.morphologyEx(openedY, cv2.MORPH_CLOSE, strelY2)

#cv2.imshow("Yellow Hue", yelHue)
#cv2.imshow("Yellow Saturation", yelSat)
#cv2.imshow("Yellow Mask", yelMorph)

#Find Yellow Contours
_, contours, _ = cv2.findContours(yelMorph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
show_bananas = fruitImg.copy()

counterY = 0

for c in contours:
    counterY = counterY + 1    
    x, y, w, h = cv2.boundingRect(c)
    cv2.drawContours(show_bananas, [c], -1, (119, 254, 255), 3)

counterY = str (counterY)
messageYel = "I found " + counterY + " bananas"
textBanana = show_bananas.copy()
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(textBanana, messageYel, (15, 60), font, 0.5,(119, 254, 255), 2)

cv2.imshow("Banana Contours", textBanana)

#=====================================================
#Thresholding for Banana-Like Hues
hOrnLow = 13
hOrnHi = 20
sOrnLow = 165
sOrnHi = 205

ret, ornH = cv2.threshold(H, hOrnLow, 255, cv2.THRESH_BINARY)
ret, ornH2 = cv2.threshold(H, hOrnHi, 255, cv2.THRESH_BINARY_INV)
ornMask = cv2.bitwise_and(ornH, ornH2)

#ret, ornS = cv2.threshold(S, sOrnLow, 255, cv2.THRESH_BINARY)
#ret, ornS2 = cv2.threshold(S, sOrnHi, 255, cv2.THRESH_BINARY_INV)
#ornSat = cv2.bitwise_and(ornS, ornS2)
#
#ornMask = cv2.bitwise_and(ornHue, ornSat)

strelO = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
openedO = cv2.morphologyEx(ornMask, cv2.MORPH_OPEN, strelO)
strelO2 = cv2.getStructuringElement(cv2.MORPH_RECT, (23, 23))
ornMorph = cv2.morphologyEx(openedO, cv2.MORPH_CLOSE, strelO2)

cv2.imshow("Orange Hue", ornMask)
cv2.imshow("Orange Mask", ornMorph)

#Find Orange Contours
_, contours, _ = cv2.findContours(ornMorph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
show_oranges = fruitImg.copy()

counterO = 0

for c in contours:
    counterO = counterO + 1    
    x, y, w, h = cv2.boundingRect(c)
    cv2.drawContours(show_oranges, [c], -1, (47, 113, 234), 3)

counterO = str (counterO)
messageOrn = "I found " + counterO + " oranges"
textOrange = show_oranges.copy()
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(textOrange, messageOrn, (15, 60), font, 0.5,(47, 113, 234), 2)

cv2.imshow("Orange Contour", textOrange)

cv2.waitKey(0)
