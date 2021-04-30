#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:22:05 2021

@author: jordan
"""
import numpy
from scipy.io import wavfile


#Replace this with your respective absolute file path for your github repo with the noisy data
github_path = "/home/jordan/Documents/UniversityStuff/2021/Stat3007/STAT3007_Project/"


#Have the noisey_names.txt file in the same location as the noisy data
names = open(github_path + "noisey_names.txt", 'r')

lines = names.readlines()

#Audios has tuple pairs of all the noisy data sounds and time with sounds first and time second
audios = []

for line in lines:
    audios.append(line[:len(line)-1])
    
data = []

for audio in audios:
    #Read file and get sampling freq [ usually 44100 Hz ]  and sound object
    samplingFreq, mySound = wavfile.read(audio)
    
    #Check if wave file is 16bit or 32 bit. 24bit is not supported
    mySoundDataType = mySound.dtype
    
    #We can convert our sound array to floating point values ranging from -1 to 1 as follows
    
    mySound = mySound
    
    #Check sample points and sound channel for duel channel(5060, 2) or  (5060, ) for mono channel
    
    mySoundShape = mySound.shape
    samplePoints = float(mySound.shape[0])
    
    #Get duration of sound file
    signalDuration =  mySound.shape[0] / samplingFreq
    
    #Plotting the tone
    
    # We can represent sound by plotting the pressure values against time axis.
    #Create an array of sample point in one dimension
    timeArray = numpy.arange(0, samplePoints, 1)
    
    #
    timeArray = timeArray / samplingFreq
    
    #Scale to milliSeconds
    timeArray = timeArray * 1000
    
    data.append((mySound, timeArray))
    
    