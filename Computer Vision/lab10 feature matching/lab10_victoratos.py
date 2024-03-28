# -*- coding: utf-8 -*-
'''
Lab 10: Feature matching starter code
Scott Spurlock 3/5/18
'''

import numpy as np
import cv2

img1 = cv2.imread('alamance.jpg')
img2 = cv2.imread('alamance_crop_rot.jpg')

# Copy images for later display
disp_img1 = img1.copy()
disp_img2 = img2.copy()

# SIFT works on grayscale images
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# SIFT settings
nFeatures = 0
nOctaveLayers = 5
contrastThreshold = .04  # Threshold to filter out weak features
edgeThreshold = 15  # Threshold to filter out edges (lower is stricter)
sigma = 1.6  # The gaussian std dev at octave zero

# Create SIFT object
sift = cv2.xfeatures2d.SIFT_create(nFeatures, nOctaveLayers, contrastThreshold,
                                   edgeThreshold, sigma)

# Detect keypoints and compute their descriptors
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

if des2 is None:
    print('No keypoints found for image 2')

else:
    # Find matches between keypoints in the two images.
    bf = cv2.BFMatcher()
    matches = bf.match(des1, des2)

    if len(matches) == 0:
        print('No matches')
    else:
        # matches is a list. Each item includes:
        # - queryIdx: which keypoint from img1 matched
        # - trainIdx: which keypoint from img2 matched
        # - distance: how (dis)similar the two keypoint descriptors are
        # We can sort the matches by the distance so that the closest matches
        # are first.
        matches = sorted(matches, key=lambda x:x.distance)

        num_matches_to_show = 5

        # Loop through the top matches
        for i in range(num_matches_to_show):
            match = matches[i]
            
            print('Match', i, ', between keypoint', match.queryIdx, 
                  'and keypoint', match.trainIdx)
            print('   distance between these keypoint descriptors is',
                  match.distance)
                  
            curr_kp1 = kp1[match.queryIdx]  # get the keypoint for img1
            size1 = curr_kp1.size
            angle1 = curr_kp1.angle
            loc1 = curr_kp1.pt
            x1 = int(loc1[0])
            y1 = int(loc1[1])

            curr_kp2 = kp2[match.trainIdx]  # get the keypoint for img2
            size2 = curr_kp2.size
            angle2 = curr_kp2.angle
            loc2 = curr_kp2.pt
            x2 = int(loc2[0])
            y2 = int(loc2[1])
            
            # TODO #1: print out keypoint angle, size, and location.
            print('The keypoint angle for img1 is ', angle1, ' , is ', size1, ' size and is located at ', loc1)
            print('The keypoint angle for img2 is ', angle2, ' , is ', size2, ' size and is located at ', loc2)

            # TODO #2: draw keypoint from img1 on disp_img1,
            # and from img2 on disp_img2

            cv2.circle(disp_img1, (x1, y1), int(size1), (26, 186, 255), 1)
            cv2.circle(disp_img2, (x2, y2), int(size2), (52, 116, 252), 1)
            
            # TODO #3: Estimate transformation - how was img2 transformed?
            # Estimate the angle it was rotated and the amount it was scaled
            # by comparing keypoint sizes and angles
            angleDiff = angle1 - angle2
            angleDiff = round(angleDiff, 2)
            
            sizeDiff = size2 / size1
            sizeDiff = round(sizeDiff, 2)
            
            print()
            print('img2 is ', angleDiff, ' degrees rotated compared to img1')
            
            print()
            print('img2 is ', sizeDiff, ' times smaller than img1')
            print()

cv2.imshow('Image 1', disp_img1)
cv2.imshow('Image 2', disp_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()