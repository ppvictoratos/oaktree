#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:29:51 2018

@author: pvictoratos

get stack overflow info

Disregard the spelling of some of my variables
"""

import numpy as np
import cv2
from os import listdir
from os.path import isfile, join
import os

#full_img = cv2.imread('map_full.jpg')
#full_img = cv2.imread('hawaii_full.jpg')
#full_img = cv2.imread('trains_full.jpg')

full_img = cv2.imread('map_small.jpg')

#path= '/Users/pvictoratos/Desktop/hw04files/map/pieces_aligned'
path= '/Users/pvictoratos/Desktop/hw04files/map/pieces_random'

peices = [ p for p in listdir(path) if isfile(join(path,p)) ]
images = np.empty(len(peices), dtype=object)

# SIFT settings for guide image
nFeatures = 0
nOctaveLayers = 12
contrastThreshold = .001  # Threshold to filter out weak features
edgeThreshold = 15  # Threshold to filter out edges (lower is stricter)
sigma = 1  # The gaussian std dev at octave zero

# SIFT settings for puzzle peices
nFeats = 0
nOctLayers = 10
contrast = .004
edges = 10

# Create SIFT objects
sift = cv2.xfeatures2d.SIFT_create(nFeatures, nOctaveLayers, contrastThreshold,
                                   edgeThreshold, sigma)
sift2 = cv2.xfeatures2d.SIFT_create(nFeats, nOctLayers, contrast, edges, sigma)


def read_in_pieces(folder):
    os.chdir(folder)
    files = []
    
    for n in os.listdir():
        puzzle_peice = cv2.imread(n)
        files.append(puzzle_peice)
    return files
        
def rotate_img(img, angle, scale):
    rows, cols = img.shape[:2]
    img_center = (rows//2, cols//2)
    M = cv2.getRotationMatrix2D(img_center, angle, scale)
    rotated = cv2.warpAffine(img, M, (cols, rows))
    return rotated
    
def version0(peices, guide):
    
    h, w = guide.shape[:2]
    print(h)
    print(w)
    
    blank = np.zeros((h, w, 3), np.uint8)
    
    gray_guide = cv2.cvtColor(guide, cv2.COLOR_BGR2GRAY)
    
    keypoints = sift.detect(gray_guide, None)
    img_disp = guide.copy()
    img_disp = cv2.drawKeypoints(img_disp, keypoints, None, color=(255, 255, 0), flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    kp1, des1 = sift.detectAndCompute(gray_guide, None)
    jigsaws = read_in_pieces(path) 
    
    for n in jigsaws:
        gray_peices = cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)
        kp2, des2 = sift.detectAndCompute(gray_peices, None)
        
        if des2 is None:
            print('No keypoints found for image 2')
            break
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

            num_matches_to_show = 2

        # Loop through the top matches
            for i in range(num_matches_to_show):
                match = matches[i]
            
                curr_kp1 = kp1[match.queryIdx]  # get the keypoint for img1
                loc1 = curr_kp1.pt
                x1 = int(loc1[0])
                y1 = int(loc1[1])

                x3 = (x1//50)*50
                y3 = (y1//50)*50

                blank[y3:y3+50, x3:x3+50] = n
                cv2.imshow('Matches', blank)
                cv2.waitKey(1)
    
    cv2.imshow('Keypoints Located', img_disp)
    
def version1(peices, guide):
    
    h, w = guide.shape[:2]
    print(h)
    print(w)
    
    blank = np.zeros((h, w, 3), np.uint8)
    
    gray_guide = cv2.cvtColor(guide, cv2.COLOR_BGR2GRAY)
    
    keypoints = sift.detect(gray_guide, None)
    img_disp = guide.copy()
    img_disp = cv2.drawKeypoints(img_disp, keypoints, None, color=(255, 255, 0), flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    kp1, des1 = sift.detectAndCompute(gray_guide, None)
    jigsaws = read_in_pieces(path) 
    
    for n in jigsaws:
        gray_peices = cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)
        kp2, des2 = sift.detectAndCompute(gray_peices, None)
        
        if des2 is None:
            print('No keypoints found for image 2')
            break
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

            num_matches_to_show = 2

        # Loop through the top matches
            for i in range(num_matches_to_show):
                match = matches[i]
            
                curr_kp1 = kp1[match.queryIdx]  # get the keypoint for img1
                loc1 = curr_kp1.pt
                angle1 = curr_kp1.angle
                x1 = int(loc1[0])
                y1 = int(loc1[1])
                
                curr_kp2 = kp2[match.trainIdx]
                angle2 = curr_kp2.angle

                angle_diff = angle2-angle1
                angle_diff = round(angle_diff, 0)
                
                if angle_diff < 0:
                    angle_diff += 360                
                
                #turns near 0 degree peices to 0
                if 0 <= angle_diff < 1:
                    rotated = rotate_img(n, 0, 1)   
                
                #turns near 90 degree peices to 90
                if 85 < angle_diff < 95:
                    rotated = rotate_img(n, 90, 1)                    
                
                #turns near 180 degree peices to 180
                if  175 < angle_diff < 185:
                    rotated = rotate_img(n, 180, 1)                    
                
                #turns near 270 degree peices to 270
                if 265 < angle_diff < 275:
                    rotated = rotate_img(n, 270, 1)                    

                x3 = (x1//50)*50
                y3 = (y1//50)*50

                blank[y3:y3+50, x3:x3+50] = rotated
                cv2.imshow('Matches', blank)
                cv2.waitKey(1)
    
    cv2.imshow('Keypoints Located', img_disp)

def version2(peices, guide):
    
    h, w = guide.shape[:2]
    print(h)
    print(w)
    
    blank = np.zeros((h, w, 3), np.uint8)
    
    gray_guide = cv2.cvtColor(guide, cv2.COLOR_BGR2GRAY)
    
    keypoints = sift.detect(gray_guide, None)
    img_disp = guide.copy()
    img_disp = cv2.drawKeypoints(img_disp, keypoints, None, color=(255, 255, 0), flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    kp1, des1 = sift.detectAndCompute(gray_guide, None)
    jigsaws = read_in_pieces(path) 
    
    for n in jigsaws:
        gray_peices = cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)
        kp2, des2 = sift.detectAndCompute(gray_peices, None)
        
        if des2 is None:
            print('No keypoints found for image 2')
            break
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

            num_matches_to_show = 2

        # Loop through the top matches
            for i in range(num_matches_to_show):
                match = matches[i]
            
                curr_kp1 = kp1[match.queryIdx]  # get the keypoint for img1
                loc1 = curr_kp1.pt
                angle1 = curr_kp1.angle
                x1 = int(loc1[0])
                y1 = int(loc1[1])
                
                curr_kp2 = kp2[match.trainIdx]
                angle2 = curr_kp2.angle

                angle_diff = angle2-angle1
                angle_diff = round(angle_diff, 0)
                
                if angle_diff < 0:
                    angle_diff += 360                
                
                #turns near 0 degree peices to 0
                if 0 <= angle_diff < 1:
                    rotated = rotate_img(n, 0, 1)   
                
                #turns near 90 degree peices to 90
                if 85 < angle_diff < 95:
                    rotated = rotate_img(n, 90, 1)                    
                
                #turns near 180 degree peices to 180
                if  175 < angle_diff < 185:
                    rotated = rotate_img(n, 180, 1)                    
                
                #turns near 270 degree peices to 270
                if 265 < angle_diff < 275:
                    rotated = rotate_img(n, 270, 1)                    

                x3 = (x1//50)*50
                y3 = (y1//50)*50

                blank[y3:y3+50, x3:x3+50] = rotated
                cv2.imshow('Matches', blank)
                cv2.waitKey(1)
    
    cv2.imshow('Keypoints Located', img_disp)
    
#version0(images, full_img)
#version1(images, full_img)     
version2(images, full_img)
cv2.waitKey(0) 
       