#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:11:02 2018

@author: pvictoratos
"""
import cv2
from PIL import Image

full_Opac = Image.open('wonka1.png')
Opac75 = full_Opac.copy()
Opac50 = full_Opac.copy()
Opac25 = full_Opac.copy()

Opac75.putalpha(191)
Opac50.putalpha(128)
Opac25.putalpha(64)

Opac75.save("C:/Users/pvictoratos/Desktop")

cv2.waitKey(0)
