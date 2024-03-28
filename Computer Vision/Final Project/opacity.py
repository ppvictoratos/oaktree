#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:11:02 2018

@author: pvictoratos
"""

from PIL import Image, ImageEnhance

img = Image.open('wonka3.png')
img = img.convert('RGBA')
opac_max = 1

#This creates a new image with an altered opacity level
def mixed_Opacities(im, opacity):
    assert opacity >= 0 and opacity <= 1
    alpha = img.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

#Runs the mixed image decrementing its opacity each time, saves to desktop
for i in range(5):
    opac = opac_max - 0.20
    sevnfive = mixed_Opacities(img, opac)
    sevnfive.save('wonka3 ' + str(i + 1) + '.png')


#Content Gif
#get an input gif and split into images
#apply style transfer from different opacities of styles to the gif