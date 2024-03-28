'''
Scott Spurlock 3/11/18
Example of using a webcam.
'''
import numpy as np
import cv2

# For a video, give the path, for a webcam, this is usually 0 or 1
vid = cv2.VideoCapture(0)
sketchOn = False
paintOn = False
cartoonOn = False
index = 0

# Use a named window to enable resizing
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

# Loop forever, getting the next frame from the camera
while True:
    ret, frame = vid.read()

    if not ret:
        print('Error reading frame')
        break

    if sketchOn == True:
        frame = cv2.medianBlur(frame, 5)
        frame = cv2.Laplacian(frame, cv2.CV_64F, ksize=5)
        frame = np.abs(frame)
        frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        kernel = np.ones((5,5), np.uint8)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, frame = cv2.threshold(frame, 15, 255, cv2.THRESH_BINARY_INV)
            
    if paintOn == True:
        frame = cv2.resize(frame, None, fx=0.25, fy= 0.25)
        for index in range (8):
            frame = cv2.bilateralFilter(frame, 8, 35, 60)
        frame = cv2.resize(frame, None, fx= 4, fy = 4)
        
    if cartoonOn == True:
        #painting
        frame = cv2.resize(frame, None, fx=0.25, fy= 0.25)
        for index in range (8):
            frame = cv2.bilateralFilter(frame, 8, 35, 60)
        frame = cv2.resize(frame, None, fx= 4, fy = 4)
        
        #sketching
        frame = cv2.medianBlur(frame, 5)
        frame = cv2.Laplacian(frame, cv2.CV_64F, ksize=5)
        frame = np.abs(frame)
        frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        kernel = np.ones((5,5), np.uint8)
        ret, frame = cv2.threshold(frame, 15, 255, cv2.THRESH_BINARY_INV)
        
    cv2.imshow('Video', frame)

    # Get any keyboard input
    key = cv2.waitKey(1)
    
    # Compare the low-order byte from the keyboard to the letter 'q'
    if 'q' == chr(key & 255):
        print('quitting...')
        break
    
    if 's' == chr(key& 255):
        sketchOn = not sketchOn
        
    if 'p' == chr(key & 255):
        paintOn = not paintOn
        
    if 'w' == chr(key & 255):
        print('screen capture')
        cv2.imwrite('ScreenCap', frame)
        
    if 'c' == chr(key & 255):
        cartoonOn = not cartoonOn
        sketchOn = False
        paintOn = False
    
# Clean up
vid.release()
cv2.destroyAllWindows()
