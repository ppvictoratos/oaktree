'''
CSC 372 Computer Vision
Homework 1: Restoring the Russian Empire
This is the starter code. Replace this with your better comments.
Author:
Date:
'''

import numpy as np
import cv2

def translate(I, x, y):
    ''' Translate the given image by the given offset in the x and y directions.
    '''
    
    # Make a transformation matrix
    M = np.float32([[1,0,x],[0,1,y]])
    
    # Get the number of rows and columns
    rows, cols = I.shape[:2]

    # Shift the image by the given offset. watch out for x,y vs. row,col
    shifted = cv2.warpAffine(I, M, (I.shape[1], I.shape[0]))

    # return the translated image
    return shifted

def compute_ssd(I1, I2):
    ''' Compute the sum-of-squared differences between two images.

    Find the difference between the images (subtract), square the difference,
    and then sum up the squared differences over all the pixels. This should
    require no explicit loops. Potentially helpful method: np.sum().

    Think carefully about math and data types.
    '''
    # TODO: return the sum-of-squared-differences (one number)
    sumSquared = I1[:,:,:3] - I2[:,:,:3] ** 2
    
    return np.sum(sumSquared)

def align_images(I1, I2):
    ''' Compute the best offset to align the second image with the first.

     Loop over a range of offset values in the x and y directions. (Use nested
     for loops.) For each possible (x, y) offset, translate the second image
     and then check to see how well it lines up with the first image using the
     SSD. 
     
     Return the aligned second image.
    '''
    # TODO:
    


# --------------------------------------------------------------------------

# this is the image to be processed
image_name = 'test.jpg'

# Read in the input image and convert to grayscale.
# TODO:

gray = cv2.cvtColor(image_name, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

# Extract the color channels.
# Note that The 3 color channels are stacked vertically.
# The blue channel is the top third of the image, the green channel is the
# middle third, and the red channel is the bottom third.
# TODO:

# First align the green channel with the blue.
# TODO: call align_images

# Next align the red channel with the blue.
# TODO: call align_images

# Merge the three color channels into a single color image.
# TODO:

cv2.watiKey(0)
# Save aligned color image to disk.
# TODO:
