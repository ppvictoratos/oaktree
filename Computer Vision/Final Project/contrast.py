#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 19:52:05 2018

@author: pvictoratos
"""

import cv2
import numpy as np

in_img = cv2.imread('cockatoo.jpg')
gray = cv2.cvtColor(in_img, cv2.COLOR_BGR2GRAY)

sob_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sob_y = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
grad_mag = np.sqrt(sob_x**2 + sob_y**2)
grad_mag = np.clip(grad_mag, 0, 255).astype(np.uint8)

cv2.imshow('Gradient Magnitude', grad_mag)
cv2.waitKey(0)