#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 19:49:29 2018

@author: Pvictoratos
"""
import numpy as np
import cv2
from os import listdir
import os

pos_path= '/Users/pvictoratos/Desktop/hw05/data/positive/train'
neg_path = '/Users/pvictoratos/Desktop/hw05/data/negative/train'
pos_test_path = '/Users/pvictoratos/Desktop/hw05/data/positive/test'
neg_test_path = '/Users/pvictoratos/Desktop/hw05/data/negative/test'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img_list = []
test_list = []

def read_in_train(path1, path2):
    label_list_training = []
    
    for n in os.listdir(path1):
        if n.startswith('.'):
            continue
        n = os.path.join(path1, n)
        test_image = cv2.imread(n)
        test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
        test_image = cv2.resize(test_image, (150, 150))
        img_list.append(test_image)
    
    print(len(img_list))
    label_list_training += len(img_list) * [1]
    print(len(label_list_training))
    
    for n in os.listdir(path2):
        if n.startswith('.'):
            continue
        n = os.path.join(path2, n)
        test_image = cv2.imread(n)
        test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
        test_image = cv2.resize(test_image, (150, 150))
        img_list.append(test_image)
    
    print(len(img_list))
    label_list_training += (len(img_list)-len(label_list_training)) * [0]
    print(len(label_list_training))
        
    labels_train = np.array(label_list_training)
    
    return labels_train, img_list

#Shows average face from model
def show_mean_face(test_model):
    m = test_model.getMean()
    m = np.reshape(m, (150,150))
    m = cv2.normalize(m, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    cv2.imshow('Mean Face', m)
    cv2.waitKey(0)
    
def show_eigen_faces(test_model):
    eigen_vecs = test_model.getEigenVectors()
    for i in range(3):
        f = np.reshape(eigen_vecs[:, i], (150, 150))
        f = cv2.normalize(f, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        cv2.imshow('Eigenface', f)
        cv2.waitKey(0)
        
labels_train, faces_list_training = read_in_train(pos_path, neg_path)

print(labels_train)

model = cv2.face.EigenFaceRecognizer_create()
model.train(faces_list_training, labels_train)
show_mean_face(model)
show_eigen_faces(model)

def testing(path3, path4):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    
    #for positive test images, 0s = fp, 1s = tp
    for n in os.listdir(path3):
        if n.startswith('.'):
            continue
        n = os.path.join(path3, n)
        test_image = cv2.imread(n)
        test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
        test_image = cv2.resize(test_image, (150, 150))
        pred_label, confidence = model.predict(test_image)
        if pred_label == 0:
            fn += 1
        if pred_label == 1:
            tp += 1
        test_list.append(test_image)
    
    #for negative test images, 0s = tn, 1s = fp
    for n in os.listdir(path4):
        if n.startswith('.'):
            continue
        n = os.path.join(path4, n)
        test_image = cv2.imread(n)
        test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
        test_image = cv2.resize(test_image, (150, 150))
        pred_label, confidence = model.predict(test_image)
        if pred_label == 0:
            fp += 1
        if pred_label == 1:
            tn += 1
        test_list.append(test_image)
    
    print(len(img_list))
    
    precision = 'Precision: ' + str(round (tp / (fp+fp), 2))
    recall = 'Recall: ' + str(round((tp/(tp+fn)),2))
    accuracy = 'Accuracy: ' + str(round ((tp + tn) / (tp + tn + fp + fn), 2))
    
    print(precision)
    print(recall)
    print(accuracy)

testing(pos_test_path, neg_test_path)

def live_demo(boolean):
    vid = cv2.VideoCapture(0)
    imgName = 1
    count = 1
    
    if boolean == True:
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
            face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        
            for (x, y, w, h) in face_rects:
                # Draw a rectangle around the detected face
                disp = cv2.rectangle(disp, (x, y), (x+w, y+h), (100, 200, 0), 2)
                disp = cv2.resize((150,150), disp)
        
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
    
        
    vid.release()
    cv2.destroyAllWindows()



#curr_gray_face_image is image in question



#unsure how to make the program count the amount of true/fase positive/negatives
#while comparing to its original positivity or negativit