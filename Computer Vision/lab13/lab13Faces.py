'''
Peter Victoratos 3/23/18
Sample of face detection in video.
Make sure you have a trained model file in the directory. If needed,
download from https://github.com/opencv/opencv/tree/master/data/haarcascades
'''

import cv2

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# For a video, give the path; for a webcam, this is usually 0 or 1
vid = cv2.VideoCapture(0)
imgName = 1
count = 1

# Loop forever (until user presses q)
while True:
    # Read the next frame from the camera
    ret, frame = vid.read()

    # Check the return value to make sure the frame was read successfully
    if not ret:
        print('Error reading frame')
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Copy the current frame for later display
    disp = frame.copy()
    
    # Detect faces in the gray image. (Lower numbers will detect more faces.)
    # Parameters:
    #   scaleFactor – Parameter specifying how much the image size is reduced at each image scale.
    #   minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.
    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)

    # loop through detected face rectangles. Each rectangle is a tuple of 4
    # numbers: the x and y position of the top-left corner and the width and
    # height of the face.
    for (x, y, w, h) in face_rects:
        # Draw a rectangle around the detected face
        disp = cv2.rectangle(disp, (x, y), (x+w, y+h), (100, 200, 0), 2)

    cv2.imshow('Video', disp)

    # Get which key was pressed
    key = cv2.waitKey(1)

    # Keep looping until the user presses q
    if key & 0xFF == ord('q'):
        break

    # TODO: when user presses 's', save the current frame
    if 's' == chr(key& 255): 
        cv2.imwrite("00" + str(imgName) + ".jpg", disp)
        imgName += 1
        
    for (x, y, w, h, count) in face_rects:
        if True:
            newFace = frame[y:y+h, x:x+w]
            newFace = 
        face + str(count) = frame[y:y+h, x:x+w]
        

vid.release()
cv2.destroyAllWindows()
