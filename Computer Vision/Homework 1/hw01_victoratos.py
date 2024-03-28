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

''' CHALLENGE 1: Modify your SSD method to only consider pixels in the center of the images. We might expect that pixels near the edges would be “noisier” and likely to adversely affect our alignment, so by using a mask or array slicing to ignore some pixels, we might get better results. Up to 2 points.'''

'''	
rows, cols = I1.shape[:2]
rows2, cols2 = I2.shape[:2]

halfwayX = rows // 2
halfwayY = cols // 2

halfwayX2 = rows2 // 2
halfwayY2 = cols2 // 2

sumSquared = I1[:halfwayX, :halfwayY, :3] - I2[:halfwayX2, :halfwayY2, :3] ** 2
return np.sum(sumSquared)
'''

# CHALLENGE 1.5: Download more images from the archive and evaluate results

''' CHALLENGE 2: 
Capture your own red, green, and blue filtered images and run your algorithm to align them. You should find a way to actually tint images red, green, and blue (for example by covering the camera with transparent, colored plastic) and take 3 different shots for the 3 different color channels. up to 2 points
'''

''' CHALLENGE 3:
Add code to show an animated visualization of the alignment process in action to illustrate what your script is doing. You might use the snow lab as inspiration. up to 3 points
'''

def align_images(I1, I2):
    ''' Compute the best offset to align the second image with the first.

     Loop over a range of offset values in the x and y directions. (Use nested
     for loops.) For each possible (x, y) offset, translate the second image
     and then check to see how well it lines up with the first image using the
     SSD. 
     
     Return the aligned second image.
    '''
    # TODO:

	x_values = [0:200]
	y_values = [0:200]

	ssd = compute_ssd(I1, I2)

	for i in x_values:
		for j in y_values:
			ssd2 = compute_ssd(i, j)
			if ssd2 < ssd, ssd == ssd2
			else, j + 1
		i + 1
	return ssd

# --------------------------------------------------------------------------

# this is the image to be processed
image_name = 'test.jpg'

# Read in the input image and convert to grayscale.
# TODO:

img = cv2.imread('test.jpg')
rows, cols = img.shape[:2]

cv2.imshow("Grayscale", img)

# Extract the color channels.
# Note that The 3 color channels are stacked vertically.
# The blue channel is the top third of the image, the green channel is the
# middle third, and the red channel is the bottom third.
# TODO:

#b, g, r = cv2.split(img) 

# Here I will split the image into thirds so I can assign each it's respective
# color channel

x = rows//3
y = (2*rows)//3
z = x+y

blue = img[0:x, cols]
green = img[x:y, cols]
red = img[y:z, cols]

#To make sure that the image is split into thirds
cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)

# First align the green channel with the blue.
# TODO: call align_images

align_images(blue, green)

# Next align the red channel with the blue.
# TODO: call align_images

align_images(blue, red)

# Merge the three color channels into a single color image.
# TODO:

merged = cv2.merge([blue, green, red])
cv2.imshow("Merged", merged)

cv2.waitKey(0)

# Save aligned color image to disk.
# TODO:

cv2.imwrite("Merged", merged)
