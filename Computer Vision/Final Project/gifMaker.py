#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 19:51:38 2018

The function that takes our mixed images of different styles and combines them

@author: pvictoratos
"""
from PIL import Image
import imageio

flowPath = '/Users/pvicoratos/Desktop/images/flow'

def image_flow(mixed_opacities):
    count = 0 
    for x in range(2):
        for i in range(5):
            img1 = Image.open('wonka' + str(x) + ' ' + str(i) + '.png')
            img1 = img1.convert('RGBA')
            img2 = Image.open('wonka' + str(x + 1) + ' ' + str(5 - i) + '.png')
            img2 = img2.convert('RGBA')
            count = count + 1
            Image.alpha_composite(img1, img2).save('mixed' + str(count) + '.png')
            
#read in flow of images from a folder called 'flow'
def gif_maker():
    images = []
    for i in range(10):
        #iteration = cv2.cvtColor(iteration, cv2.COLOR_RGBA2BGR)
        images.append(imageio.imread('mixed' + str(i + 1) + '.png'))
    imageio.mimwrite('/Users/pvictoratos/Desktop/wonka.gif', images)
    
gif_maker()