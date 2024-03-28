'''
Peter Victoratos 4/16/18
Lab 18: CNN
'''
import time
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from datasetloader import DatasetLoader

# model file
model_file = 'tensorflow_inception_graph.pb'
labels_file = 'imagenet_comp_graph_label_strings.txt'
image_size = (224, 224)
mean_color = (104, 117, 123)

# Path to top-level image folder.
base_path = '/Users/pvictoratos/Desktop/animals'
learning_rate = 0.0001
use_cnn = False
num_filters1 = 32
num_filters2 = 64
num_hidden_units = 1024
max_iter = 15
dropout_rate = 0

# Object to load dataset.
dl = DatasetLoader(base_path, image_size)
# Create object to load dataset.
filename = 'grom.jpg'

# Read in the images. This may take a while if there are a lot of large images.
print("Loading data...")
start_time = time.clock()
(data, labels) = dl.load(verbose=500)
print('Seconds elapsed: {:.2f}'.format(time.clock() - start_time))


#---------------------------------------------------------------------------
print('Loading labels file...')
classes = open(labels_file).read().strip().split("\n")

print('Loading model file...')
net = cv2.dnn.readNetFromTensorflow(model_file)

print('Reading in image...')

# Split the data into training and testing sets using 75% of
# the data for training and the remaining 25% for testing
(X_train, X_test, Y_train, Y_test) = train_test_split(data, labels, test_size=0.25)

X_mean = X_train.mean(axis=0)
X_train = X_train - X_mean
X_test = X_test - X_mean
Y_pred = []

for x in range(len(x)):
    blob = cv2.dnn.blobFromImage(x, 1, image_size, mean_color)
    net.setInput(blob)
    probs = net.forward()
    probs = probs[0]
    # Sort the indexes of the probabilities
    idxs = np.argsort(probs)
    # Reverse the list so that indexes of the highest probablities are first
    idxs = idxs[::-1]
    curr_class_idx = idxs[0]
    curr_class_label = classes[curr_class_idx]
    if curr_class_label == 'dog':
        Y_pred.append[0]
    if curr_class_label == 'cat':
        Y_pred.append[0]
    if curr_class_label == 'panda':
        Y_pred.append[0]
    
    
# Make and print confusion matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)
num_correct = np.diag(cm).sum()

# ------------------------------------------
# Visualize results
# ------------------------------------------
plt.figure()
plt.plot(np.array(loss_per_step), label='Loss')
plt.plot(np.array(train_acc_per_step), label='Training Accuracy')
plt.plot(np.array(test_acc_per_step), label='Testing Accuracy')
plt.legend()
#plt.ylabel('Loss')
plt.xlabel('Iteration')
plt.title('Loss & accuracy (best test accuracy {:.2f})'.format(best_test_acc))
plt.show()
