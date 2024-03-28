# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

def find_waldo (img, template):
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_waldo = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    t_height, t_width = template.shape[:2]

    method = cv2.TM_CCORR_NORMED

    res = cv2.matchTemplate(gray_img, gray_waldo, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bot_right = (top_left[0] + t_width, top_left[1] + t_height)

    resDis = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    cv2.imshow("result", resDis)
    cv2.rectangle(img, (top_left), (bot_right), (0,255,0), 3)
    return img

def find_waldo_non (img, template):
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_waldo = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    t_height, t_width = template.shape[:2]

    method = cv2.TM_CCORR

    res = cv2.matchTemplate(gray_img, gray_waldo, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bot_right = (top_left[0] + t_width, top_left[1] + t_height)
    
    resDisN = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    cv2.imshow("result non", resDisN)
    cv2.rectangle(img, (top_left), (bot_right), (0,255,0), 3)
    return img

img = cv2.imread('waldo_scene0.jpg')
imgCopy = img.copy()
img2 = cv2.imread('waldo_scene2.jpg')
imgTemp = cv2.imread('waldo.jpg')

found_him = find_waldo(img, imgTemp)
didnt_find_him = find_waldo_non(imgCopy, imgTemp)
second_img = find_waldo(img2, imgTemp)

cv2.imshow("Normalized", found_him)
cv2.imshow("Non-Normalized", didnt_find_him)
cv2.imshow("Normalized 2", second_img)

cv2.waitKey(0)