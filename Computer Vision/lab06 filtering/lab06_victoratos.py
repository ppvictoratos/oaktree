# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np

img = cv2.imread('ladybug.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img)

def add_noise(img, strength):
    rows, cols = img.shape[:2]
    randomImg = np.random.randint(-strength, strength, (rows, cols))
    img = img.astype(np.float)
    img = img + randomImg
    img = np.clip(img, 0, 255)
    img = img.astype(np.uint8)
    return img

noisy = add_noise(img, 25)

# Little bit of noise, strength is 50
cv2.imshow("Kinda Noisy", noisy)

# Little bit of noise, strength is 100
cv2.imshow("Pretty Loud", add_noise(img, 50))

#Blurring to Denoise Image
blurred = cv2.blur(noisy, (4,4))
cv2.imshow("Blurred", blurred)

#Gaussian Blurring to Denoise Image
gauss = cv2.GaussianBlur(noisy, (5,5), 0)
cv2.imshow("Gaussian Blur", gauss)

median = cv2.medianBlur(noisy, 3)
cv2.imshow("Median Filtering", median)

bilateral = cv2.bilateralFilter(noisy, 3, 35, 35)
cv2.imshow("Bilateral Filtering", bilateral)

cv2.waitKey(0)
    