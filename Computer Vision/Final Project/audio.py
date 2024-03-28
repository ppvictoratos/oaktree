#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 01:30:40 2018

@author: pvictoratos

"""

import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.io import wavfile
from scipy.signal import argrelextrema
import cv2

myAudio = 'bounce 2.wav'

#Read file and get sampling freq [ usually 44100 Hz ]  and sound object
samplingFreq, mySound = wavfile.read(myAudio)

#Check if wave file is 16bit or 32 bit. 24bit is not supported
mySoundDataType = mySound.dtype

#We can convert our sound array to floating point values ranging from -1 to 1 as follows

mySound = mySound / (2.**15)

#Check sample points and sound channel for duel channel(5060, 2) or  (5060, ) for mono channel

mySoundShape = mySound.shape
samplePoints = float(mySound.shape[0])

#Get duration of sound file
signalDuration =  mySound.shape[0] / samplingFreq

#If two channels, then select only one channel
mySoundOneChannel = mySound[:,0]

#Plotting the tone

# We can represent sound by plotting the pressure values against time axis.
#Create an array of sample point in one dimension
timeArray = numpy.arange(0, samplePoints, 1)

#
timeArray = timeArray / samplingFreq

#Scale to milliSeconds
timeArray = timeArray * 1000

#Plot the tone
plt.plot(timeArray, mySoundOneChannel, color='G')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.show()

maxInd = argrelextrema(timeArray, numpy.greater)
rel = timeArray[maxInd]
print(rel)

#caveman way to get time signatures (looking)
time = 2000
time1 = time * 0.345
time2 = time * 0.625
time3 = time * 0.845

mix0 = cv2.imread('Mixed0.jpg')
mix1 = cv2.imread('Mixed1.jpg')
mix2 = cv2.imread('Mixed2.jpg')

i = 0
sw = 'yo' + str(i)

images = []

for i in range(7):
    sw = mix0.copy()
    images.append(sw)
for i in range(12):
    sw = mix0.copy()
    images.append(sw)
for i in range(17):
    sw = mix0.copy()
    images.append(sw)
    

    
### Scans a basic audio file for relative maximum spikes
#def spike_watcher(plt iamge):
    

#A little more complicated:

##Plot frequency content
##We can get frquency from amplitude and time using FFT , Fast Fourier Transform algorithm
#
##Get length of mySound object array
#mySoundLength = len(mySound)
#
##Take the Fourier transformation on given sample point 
##fftArray = fft(mySound)
#fftArray = fft(mySoundOneChannel)
#
#numUniquePoints = numpy.ceil((mySoundLength + 1) / 2.0)
#fftArray = fftArray[0:numUniquePoints]
#
##FFT contains both magnitude and phase and given in complex numbers in real + imaginary parts (a + ib) format.
##By taking absolute value , we get only real part
#
#fftArray = abs(fftArray)
#
##Scale the fft array by length of sample points so that magnitude does not depend on
##the length of the signal or on its sampling frequency
#
#fftArray = fftArray / float(mySoundLength)
#
##FFT has both positive and negative information. Square to get positive only
#fftArray = fftArray **2
#
##Multiply by two (research why?)
##Odd NFFT excludes Nyquist point
#if mySoundLength % 2 > 0: #we've got odd number of points in fft
#    fftArray[1:len(fftArray)] = fftArray[1:len(fftArray)] * 2
#
#else: #We've got even number of points in fft
#    fftArray[1:len(fftArray) -1] = fftArray[1:len(fftArray) -1] * 2  
#
#freqArray = numpy.arange(0, numUniquePoints, 1.0) * (samplingFreq / mySoundLength);
#
##Plot the frequency
#plt.plot(freqArray/1000, 10 * numpy.log10 (fftArray), color='B')
#plt.xlabel('Frequency (Khz)')
#plt.ylabel('Power (dB)')
#plt.show()
