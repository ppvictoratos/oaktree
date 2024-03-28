'''
Scott Spurlock 4/2/18
Lab 14: KNN
Adapted from Rosebrock DL4CV.
'''

import numpy as np
import time
import cv2
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from datasetloader import DatasetLoader
from sklearn.svm import LinearSVC

base_path = '/Users/pvictoratos/Desktop/animals' # Path to top-level image folder.
k = 1                             # Main hyperparameter for KNN
image_size = (32, 32)              # Make images this size

# Create object to load dataset.
dl = DatasetLoader(base_path, (32, 32))

# Read in the images. This may take a while if there are a lot of large images.
print("Loading data...")
start_time = time.clock()
(data, labels) = dl.load(verbose=500)
print('Seconds elapsed: {:.2f}'.format(time.clock() - start_time))

num_examples = data.shape[0]
dim_examples = image_size[0] * image_size[1] * 3

# Flatten images to each be one long row in a matrix of examples.
data = data.reshape((num_examples, dim_examples))

# Encode the labels as integers.
le = LabelEncoder()
labels = le.fit_transform(labels)

# Split the data into training and testing sets using 75% of
# the data for training and the remaining 25% for testing
(X_train, X_test, Y_train, Y_test) = train_test_split(data, labels, test_size=0.25)

#Initialize Model
model = MLPClassifier(activation='logistic', solver ='sgd', hidden_layer_sizes =(20), verbose = True, max_iter=100, learning_rate_init=0.1)

#Standardize Data
X_mean = X_train.mean(axis=0)
X_std = X_train.std(axis=0)
X_train = (X_train - X_mean) / X_std
X_test = (X_test - X_mean) / X_std

#Y_mean = Y_train.mean(axis=0)
#Y_std = Y_train.std(axis=0)
#Y_train = (Y_train - Y_mean) / Y_std
#Y_test = (Y_test - Y_mean) / Y_std

# Train a MLP classifier
print("Creating MLP classifier...")
start_time = time.clock()
model.fit(X_train, Y_train)
print('Seconds elapsed training: {:.2f}'.format(time.clock() - start_time))
print("Evaluating MLP classifier...")
start_time = time.clock()
Y_pred = model.predict(X_test)
print('Seconds elapsed testing: {:.2f}'.format(time.clock() - start_time))

# Calculate and print accuracy
num_right = np.count_nonzero(Y_pred == Y_test)
acc = 100 * num_right / len(Y_test)
print('accuracy = {:.2f}%'.format(acc))

# Make and print confusion matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)
num_correct = np.diag(cm).sum()

# Plot confusion matrix
plt.figure()
plt.plot(model.loss_curve_)
plt.ylabel('Loss')
plt.xlabel('Iteration')
plt.show()

