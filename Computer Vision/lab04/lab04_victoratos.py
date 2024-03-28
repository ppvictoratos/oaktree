"""
Lab04: Thresholding

Use histograms, thresholding, and masking.

Your name and date here

"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# Part 1: Grayscale histogram

# TODO: read in an image and convert to gray
img = cv2.imread('basenji.jpg')
img2 = cv2.imread('andre.jpg')
cv2.imshow("Regular Basenji", img)

#call convert color bgr to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# TODO: use cv2.calcHist to calculate the histogram of the gray image
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# TODO: plot the histogram using plt.plot
plt.plot(hist, linewidth=1)
# -------------------------------------------------------------------------
# Part 2: Making the mask

# TODO: pick a threshold value based on the histogram and threshold the image
# to create a binary image that is black for background and white for foreground.
T = 8 #threshold value
ret, thresh = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)

# Use morphological operations (open, close) to clean up the binary image.
# TODO: make a structuring element and close and open the binary image.
strel =  cv2.getStructuringElement(cv2.MORPH_RECT, (15,15))
opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, strel)
strel2 =  cv2.getStructuringElement(cv2.MORPH_RECT, (100,100))
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, strel2)

# TODO: use the binary image as a mask applied to the original image so that
# the background is blafk and the foreground is color from the original image.
mask = np.zeros(img.shape[:2], dtype = "uint8")
cv2.imshow("thresh", thresh)
cv2.imshow("closed", closed)
cv2.imshow("opened", opened)

masked = cv2.bitwise_and(img, img, mask=closed)
cv2.imshow("Mask On Image", masked)

# TODO: show the original, gray, thresholded, closed, opened, and masked images.
cv2.imwrite('gray.jpeg', gray)
cv2.imshow("Gray Basenji", gray)

#Green Screen Challenge
(B, G, R) = cv2.split(img2)
hist2 = cv2.calcHist([G], [0], None, [256], [0, 256])
T2 = 223
ret, thresh2 = cv2.threshold(G, T2, 255, cv2.THRESH_BINARY_INV)

strel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (25,25))
closed2 = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, strel3)

mask2 = np.zeros(img2.shape[:2], dtype = "uint8")
masked2 = cv2.bitwise_and(img2, img2, mask=closed2)
cv2.imshow("Mask On Andre", masked2)

cv2.imshow("Greened", thresh2)
cv2.imshow("Closed2", closed2)

#Combining Color Channels Challenge


cv2.waitKey(0)