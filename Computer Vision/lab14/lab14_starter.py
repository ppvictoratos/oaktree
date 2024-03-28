'''
Scott Spurlock 4/2/18
Lab 14: KNN
Adapted from Rosebrock DL4CV.
'''

import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from datasetloader import DatasetLoader

base_path = '/Users/pvictoratos/Desktop/flowers' # Path to top-level image folder.
k = 33                              # Main hyperparameter for KNN
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

# Train a KNN classifier
print("Creating KNN classifier...")
print("k value: " + str(k))
start_time = time.clock()
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, Y_train)
print('Seconds elapsed: {:.2f}'.format(time.clock() - start_time))
print("Evaluating KNN classifier...")
start_time = time.clock()
Y_pred = model.predict(X_test)
print('Seconds elapsed: {:.2f}'.format(time.clock() - start_time))

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
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.gray)
plt.title('Confusion Matrix')
plt.colorbar()
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
