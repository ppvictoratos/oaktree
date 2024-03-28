#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 03:17:48 2018

@author: Pvictoratos
"""
import cv2

#converts video to images
def vidImg():
    vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        count += 1
        
#grab first percentage of frames based on how far the spike in the wav is

#iterate over these percentages and compile into a video
        
#add the music back
        