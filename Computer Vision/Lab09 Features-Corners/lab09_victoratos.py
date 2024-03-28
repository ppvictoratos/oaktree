# -*- coding: utf-8 -*-
"""
Lab 9: Features

Peter Victoratos
CSC 411
March 1, 2018
"""

import cv2
import numpy as np

img1 = cv2.imread('pdc1.jpg')
img2 = cv2.imread('pdc2.jpg')

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Sobel Filtering for Image 1
sob_x1 = cv2.Sobel(gray1, cv2.CV_64F, 1, 0)
sob_y1 = cv2.Sobel(gray1, cv2.CV_64F, 1, 0)

grad_mag_1 = np.sqrt(sob_x1**2 + sob_y1**2)
grad_mag_1 = np.clip(grad_mag_1, 0, 255).astype(np.uint8)

#Sobel Filtering for Image 2
sob_x2 = cv2.Sobel(gray2, cv2.CV_64F, 1, 0)
sob_y2 = cv2.Sobel(gray2, cv2.CV_64F, 1, 0)

grad_mag_2 = np.sqrt(sob_x2**2 + sob_y2**2)
grad_mag_2 = np.clip(grad_mag_2, 0, 255).astype(np.uint8)

#Blurring and Finding Canny Images Img1
gray_smooth1 = cv2.GaussianBlur(gray1, (3,3), 0)
dst1 = cv2.Canny(gray_smooth1, 30, 150)
edge_thresh1 = dst1 > 0
img_disp1 = img1.copy()
img_disp1[edge_thresh1] = (0, 255, 255)

#Blurring and Finding Canny Images Img2
gray_smooth2 = cv2.GaussianBlur(gray2, (3,3), 0)
dst2 = cv2.Canny(gray_smooth2, 30, 150)
edge_thresh2 = dst2 > 0
img_disp2 = img2.copy()
img_disp2[edge_thresh2] = (0, 255, 255)

#Harris Corners Img1 
block1 = 2
kernel1 = 5
K1 = 0.04
dst1 = cv2.cornerHarris(gray_smooth1, block1, kernel1, K1)
thresh_val1 = 0.0001 * dst1.max()
corner_thresh1 = dst1 > thresh_val1
img_disp1B = img1.copy()
img_disp1B[corner_thresh1] = (0, 255, 0)

#Harris Corners Img2 
block2 = 2
kernel2 = 5
K2 = 0.04
dst2 = cv2.cornerHarris(gray_smooth2, block2, kernel2, K2)
thresh_val2 = 0.0001 * dst2.max()
corner_thresh2 = dst2 > thresh_val2
img_disp2B = img2.copy()
img_disp2B[corner_thresh2] = (0, 255, 0)

#SIFT Features for Img1
sift1 = cv2.xfeatures2d.SIFT_create()
keypoints1 = sift1.detect(gray1, None)
img_disp1C = img1.copy()
img_disp1C = cv2.drawKeypoints(img_disp1C, keypoints1, None, color=(255,255,0), 
                               flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#SIFT Features for Img2
sift2 = cv2.xfeatures2d.SIFT_create()
keypoints2 = sift2.detect(gray2, None)
img_disp2C = img2.copy()
img_disp2C = cv2.drawKeypoints(img_disp2C, keypoints2, None, color=(255,255,0), 
                               flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#Display my Images
cv2.imshow("Original 1", img1)
cv2.imshow("Original 2", img2)
cv2.imshow("Grad Mag 1", grad_mag_1)
cv2.imshow("Grad Mag 2", grad_mag_2)
cv2.imshow("Blurred/Canny 1", img_disp1)
cv2.imshow("Blurred/Canny 2", img_disp2)
cv2.imshow("Harris Corners 1", img_disp1B)
cv2.imshow("Harris Corners 2", img_disp2B)
cv2.imshow("SIFT 1", img_disp1C)
cv2.imshow("SIFT 2", img_disp2C)

cv2.waitKey(0)