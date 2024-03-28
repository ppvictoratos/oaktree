# -*- coding: utf-8 -*-
import numpy as np
import cv2

image_name = 'zoidberg.jpg'
image2_name = 'billyMandy.jpg'
img2 = cv2.imread(image2_name)
img = cv2.imread(image_name)

rows, cols = img.shape[:2]
image_center = (rows//2, cols//2)

rows2, cols2 = img2.shape[:2]
image2_center = (rows2//2, cols//2)

def translate_image(img, x, y):
    M = np.float32([[1,0,x],[0,1,y]])
    shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return shifted

def rotate_image(img, angle, scale):
    M = cv2.getRotationMatrix2D(image_center, angle, scale)
    rotated = cv2.warpAffine(img, M, (cols, rows))
    return rotated

def filter_image(img):
    filtered = img.astype(np.float)
    halfX = image_center[0]
    halfY = image_center[1]
    
    #Increase Contrast by 1.5
    filtered[0:halfX, 0:halfY] *= 1.5
    
    #Descrease Contrast by 1.5
    filtered[halfX:rows, 0:halfY] /= 1.5
    
    #Brighten by 128
    filtered[0:halfX, halfY:cols] += 128
    
    #Invert Colors
    filtered[halfX:rows, halfY:cols] -= 255
    
    filtered = np.clip(filtered, 0, 255)
    filtered = filtered.astype(np.uint8)
    return filtered

# Translate then Rotate Image
translatedZ = translate_image(img, -150, 100)
newZ = rotate_image(translatedZ, 45, 1.0)

cv2.imshow("Translated Zoidberg 1", newZ)

# Rotate then Translate Image
rotatedZ = rotate_image(img, 45, 1.0)
newZ2 = translate_image(rotatedZ, -150, 100)

cv2.imshow("Translated Zoidberg 2", newZ2)

# Filter Image Quadrents
filtered = filter_image(img)

cv2.imshow("Filtered Zoidberg", filtered)

mask = np.zeros((rows2, cols2), np.uint8)

masked = cv2.bitwise_and(img2, img2, mask = mask)
cv2.imshow("Mask On", masked)

cv2.waitKey(0)

