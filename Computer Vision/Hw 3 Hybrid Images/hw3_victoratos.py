# -*- coding: utf-8 -*-
"""
Spyder Editor

Peter Victoratos
CSC 411
March 7, 2018
"""

import cv2 
import numpy as np

img1 = cv2.imread('littledog.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread('cat2.jpg')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#This method creates an empty list the size of how many levels are asked for,
#it gets the size of the original image and then runs a for loop that blurs 
#the input image, and shrinks it. It adds the new image to the next position
#in the list until the number of levels is reached 

def make_gaussian_pyramid(img, levels, debug):
    gaussPyr = []
    gaussPyr.append(img)
    for x in range(1, levels):
        blur = cv2.GaussianBlur(img, (3,3), 0)
        smol = cv2.resize(blur, (0,0), fx=0.5, fy=0.5)
        img = smol
        #cv2.normalize(smol, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        gaussPyr.append(smol)
        x += 1

        if debug == True:
            cv2.imshow("Gaussian Pyramid Iterations", img)
            cv2.waitKey(1000)
        
    return gaussPyr

#This method takes an input image and creates a list of smaller, and blurrier
#variations of the original image 

def make_laplacian_pyramid(img, levels, debug):
    laplacPyr = []
    laplacPyr.append(img)
    for x in range(1, levels):
        blur = cv2.GaussianBlur(img, (3,3), 0)
        imblur = img - blur
        smol = cv2.resize(imblur, (0,0), fx=0.5, fy=0.5)
        img = smol
        #cv2.normalize(smol, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        laplacPyr.append(smol)
        x += 1

        if debug == True:
            cv2.imshow("Laplacian Pyramid Iterations", img)
            cv2.waitKey(1000)
    
    return laplacPyr
       
#Show pyramid displays the image and its smaller/blurrier iterations next to it
#all in decreasing size.
     
def show_pyramid(pyramid):
    h, w = pyramid[0].shape
    maxH = h
    #minH = maxH - 1
    halfW = w/2
    M = np.zeros([maxH, w + int(w/2)])
    m = 1
    m2 = 2
    M[0: h, 0: w] = pyramid[0]
    
    for x in range(1, len(pyramid)):
        if x % 2 == 0:
            val = 0
        else:
            val = 1
        M[maxH - int(maxH/m) : (maxH-val) - int(maxH/m2), w: w + int(halfW/m)] = pyramid[x]
        m *= 2
        m2 *= 2
        x += 1
        
    finalWindow = cv2.normalize(M, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U) 
    return finalWindow

#    pyramid[1] = M[maxH - int(maxH/1): maxH - int(maxH/2), w: int(maxW)]
#    pyramid[2] = M[maxH - int(maxH/2): maxH - int(maxH/4), w: int(maxW/2)]
#    pyramid[3] = M[maxH - int(maxH/4): maxH - int(maxH/8), w: int(maxW/4)]
#    pyramid[4] = M[maxH - int(maxH/8): maxH - int(maxH/16), w: int(maxW/8)]
    
#This method takes some laplacian levels from one image and gaussian levels from
#another image and puts them together. The resulting image is a hybrid of the two

def make_hybrid_image(near, far, levels, split):
    hFar, wFar = far[0].shape
    hNear, wNear = near[0].shape
    lap = 0
    gaus = 0
    
    for x in range(0, split):
        if near[x].shape < near[0].shape:
            near[x] = cv2.resize(near[x], (0, 0), hNear, wNear)
        lap += near[x]
        x += 1
        
    for y in range(split, levels):
        if far[x].shape < far[0].shape:
            far[x] = cv2.resize(far[x], (0, 0), hFar, wFar)
        gaus += near[x]
        y += 1

    final = lap + gaus
    veryFinal = cv2.normalize(final, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    return veryFinal


#This is where the magic happens
gP = make_gaussian_pyramid(img1, 5, False)
lP = make_laplacian_pyramid(img2, 5, False)

gPFinal = show_pyramid(gP)
lPFinal = show_pyramid(lP)

hybrid = make_hybrid_image(img1. img2, 5, 3)

cv2.imshow("Gaussian Pyramid", gPFinal)
cv2.imshow("Laplacian Pyramid", lPFinal)
cv2.waitKey(0)

