# -*- coding: utf-8 -*-
# Show pixel color values as the mouse moves around an image
# Scott Spurlock 2/12/18
# --------------------------------------------------------------------------

import numpy as np
import cv2
import os
import sys

# ====================================
# Your image name here
image_name = 'pumpkins.jpeg'
# ====================================

# For writing text
curr_position = (0, 0)
write_color = (0, 0, 0)
horiz_offset = 0
vert_offset = 20
font = cv2.FONT_HERSHEY_SIMPLEX


# This method gets called automatically anytime the mouse moves or is clicked
def mouse_event_handler(event, x, y, flags, param):
    # Tell the method about the global variables
    global curr_position, write_color

    # If the mouse moved
    if event == cv2.EVENT_MOUSEMOVE:
        curr_position = (x, y)

    # When the mouse is clicked, change text color randomly
    if event == cv2.EVENT_LBUTTONDOWN:
        write_color = np.random.randint(0, 255, 3)

        # Turn the color into a tuple
        write_color = tuple(write_color.tolist())

    # When the mouse is right-clicked, change text color to black
    if event == cv2.EVENT_RBUTTONDOWN:
        write_color = (0, 0, 0)


# ---------------------------------------------------
# Check current directory
curr_working_dir = os.getcwd()
print('\nStarting color checker in directory: {}'.format(curr_working_dir))

# Read in the image
image = cv2.imread(image_name)

# Make sure we actually read in an image
if image is None:
    print('Failed to read image file: {}\n'.format(image_name))
    sys.exit(0)

# Open a window, name it "Press q to quit", and allow it to be resized
cv2.namedWindow("Press q to quit", cv2.WINDOW_NORMAL)

# Tell OpenCV which method will handle mouse events for the window called
# "Press q to quit"
cv2.setMouseCallback("Press q to quit", mouse_event_handler)

# Loop forever (or until q is pressed)
while True:
    # Get current pixel color (x, y is backward from row, column)
    curr_color = image[curr_position[1], curr_position[0]]

    # Format the color so OpenCV likes it for conversion
    curr_color = np.reshape(curr_color, (1, 1, 3))

    # Convert to HSV
    hsv = cv2.cvtColor(curr_color, cv2.COLOR_BGR2HSV)

    # Format the colors as strings for easy disply
    bgr = str(np.reshape(curr_color, 3).tolist())
    hsv = str(np.reshape(hsv, 3).tolist())

    # Make a copy of the image to write on (we don't want to change the orig.)
    img_copy = image.copy()

    # Adjust text position based on mouse position to keep text onscreen
    if curr_position[0] > image.shape[1]/2:
        horiz_offset = -200
    else:
        horiz_offset = 0

    if curr_position[1] > image.shape[0]/2:
        vert_offset = -60
    else:
        vert_offset = 25

    # BGR
    write_pos = (curr_position[0]+horiz_offset, curr_position[1]+vert_offset)
    cv2.putText(img_copy, 'bgr ' + bgr, write_pos, font, 0.7, write_color, 2)
    # HSV
    vert_offset += 25
    write_pos = (curr_position[0]+horiz_offset, curr_position[1]+vert_offset)
    cv2.putText(img_copy, 'hsv ' + hsv, write_pos, font, 0.7, write_color, 2)

    # Display and check for keypress
    cv2.imshow("Press q to quit", img_copy)
    key = cv2.waitKey(1) & 0xFF

    # Quit when q is pressed
    if key == ord('q'):
        break

# close all open windows
cv2.destroyAllWindows()
