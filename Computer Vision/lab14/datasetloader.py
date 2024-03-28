'''
Scott Spurlock 4/2/18
Lab 14: KNN
Adapted from Rosebrock DL4CV.
'''

import numpy as np
import cv2
import os

class DatasetLoader:
    def __init__(self, base_directory=None, image_size=(32, 32)):
        '''
        Constructor requires a base directory containing subfolder, each with
        images to be loaded. The subfolder names are taken as class names.
        Images will all be resized to the given image size.
        '''
        self.base_directory = base_directory
        self.image_size = image_size

    def load(self, verbose=-1):
        ''' 
        Creates a blank numpy array to house the solved puzzle, calculates the 
        scale of completed puzzle to puzzle guide.
        
        Parameters:
        verbose: controls how often an update is displayed (every verbose
        images read). Default is -1, which means no updates are displayed.
        
        Returns:
        A 2-tuple consisting of
          - data: the images as a numpy array of size n x rows x cols x chnls,
            where n is the number of images loaded.
          - labels: 1-D numpy array of strings extracted from image folder
            names. The array will have n elements in it, corresponding to the
            n images.
        '''
        # Initialize the list of features and labels
        data = []
        labels = []

        # Get all the image filepaths based on the base directory
        image_paths = self.list_image_files()

        # Loop over the input images
        for (i, imagePath) in enumerate(image_paths):
            # load the image and extract the class label assuming
            # that our path has the following format:
            # /path/to/dataset/{class}/{image}.jpg
            image = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-2]

            # Handle any preprocessing
            image = self.preprocess_image(image)

            # treat our processed image as a "feature vector"
            # by updating the data list followed by the labels
            data.append(image)
            labels.append(label)

            # show an update every `verbose` images
            if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
                print('[INFO] processed {}/{}'.format(i + 1,
                    len(image_paths)))

        # return a tuple of the data and labels
        return (np.array(data), np.array(labels))
    
    def list_image_files(self):
        '''
        Returns all filenames (with full paths) from a search down from this
        object's base directory into the contained subfolders.
        '''
        all_filenames = []
        
        if not os.path.isdir(self.base_directory):
            raise NotADirectoryError('Input does not appear to be a directory -- ' + self.base_directory)
            
        folders = os.listdir(self.base_directory)
            
        for folder in folders:
            curr_path = os.path.join(self.base_directory, folder)
            
            filenames = os.listdir(curr_path)
            
            for filename in filenames:
                full_path = os.path.join(curr_path, filename)
                all_filenames.append(full_path)
    
        return all_filenames

    def preprocess_image(self, image):
        '''
        For this simple dataset loader, preprocessing consists only of resizing.
        '''
        return cv2.resize(image, self.image_size, interpolation=cv2.INTER_AREA)
