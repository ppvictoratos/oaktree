# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

img = cv2.imread('nyc.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

sob_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sob_x_vis = np.absolute(sob_x)
sob_x_vis = np.clip(sob_x_vis, 0, 255).astype(np.uint8)

sob_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
sob_y_vis = np.absolute(sob_y)
sob_y_vis_ = np.clip(sob_y_vis, 0, 255).astype(np.uint8)

grad_mag = np.sqrt(sob_x**2 + sob_y**2)
grad_mag= np.clip(grad_mag, 0, 255).astype(np.uint8)

gauss1 = cv2.GaussianBlur(gray, (3,3), 0)
gauss2 = cv2.GaussianBlur(gray, (17,17), 0)

canny = cv2.Canny(gray, 30, 150)
cannyBlur = cv2.Canny(gauss1, 30, 150)
cannyBlurier = cv2.Canny(gauss2, 30, 150)

grad_angle = np.arctan(sob_y/sob_x)

cv2.imshow("Sobel X", sob_x_vis)
cv2.imshow("Sobel Y", sob_y_vis)
cv2.imshow("Grad Mag", grad_mag)
cv2.imshow("Canny No Blur", canny)
cv2.imshow("Canny With Blur", cannyBlur)
cv2.imshow("Canny With More Blur", cannyBlurier)

cv2.waitKey(0)
