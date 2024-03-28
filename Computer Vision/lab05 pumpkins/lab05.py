# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

img = cv2.imread('pumpkins.jpeg')

b, g, r = cv2.split(img)

cv2.imshow("Original", img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(hsv)

cv2.imshow("Hue", H)
cv2.imshow("Saturation", S)
cv2.imshow("Value", V)

#Thresholding on the Hue Channel
T = 9 #low threshold value, lowest orange
T2 = 35 #high threshold value, highest orange
ret, thresh = cv2.threshold(H, T, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(H, T2, 255, cv2.THRESH_BINARY_INV)
threshed = cv2.bitwise_and(thresh, thresh2)

#Thresholding on the Saturation Channel
T3 = 69 #low threshold value, lowest orange
T4 = 255 #high threshold value

ret, thresh3 = cv2.threshold(S, T3, 255, cv2.THRESH_BINARY)
ret, thresh4 = cv2.threshold(S, T4, 255, cv2.THRESH_BINARY_INV)
satThresh = cv2.bitwise_and(thresh3, thresh4)

combined = cv2.bitwise_and(threshed, satThresh)
cv2.imshow("Combined No Morph", combined)

#Morphological Operations used to clean up the final mask
strel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
opened = cv2.morphologyEx(combined, cv2.MORPH_OPEN, strel)
strel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (35, 35))
morphed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, strel2)

cv2.imshow("Threshed", threshed)
cv2.imshow("Saturation Threshold", satThresh)
cv2.imshow("opened", opened)
cv2.imshow("Combined Thresholds", morphed)

#Find Contours
_, contours, _ = cv2.findContours(morphed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

show_objects = img.copy()

for c in contours:
    
    x, y, w, h = cv2.boundingRect(c)
    
    cv2.drawContours(show_objects, [c], -1, (255, 0, 255), 4)

message = "I found 4 pumpkins"
textOn = show_objects.copy()
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(textOn, message, (50, 50), font, 0.9, (0,0,0), 2)

cv2.imshow("Contours", textOn)

#Challenge 1
img2 = cv2.imread('thresh_numbers.jpg')
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
Tgray = 2

ret, threshGray = cv2.threshold(gray, Tgray, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Numbers", threshGray)
strelGray = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
blobs = cv2.morphologyEx(threshGray, cv2.MORPH_CLOSE, strel)
cv2.imshow("Blobs", blobs)

'''#Find Contours
_, contours2, _ = cv2.findContours(morphed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

show_objects = img2.copy()

for c in contours:
    
    x, y, w, h = cv2.boundingRect(c)
    
    cv2.drawContours(show_objects, [c], -1, (255, 0, 255), 4)

message1 = "I found 8 blobs"
textOn2 = show_objects.copy()
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(blobs, message1, (15, 15), font, 0.3, (255,255,255), 2)

cv2.imshow("Contours", textOn2)
'''

cv2.waitKey(0)