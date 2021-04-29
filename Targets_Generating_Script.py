#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:33:13 2021

@author: jordan
"""

import subprocess
#Change local use right click, click propertites then copy the file path to replace the below string
github_path = "/home/jordan/Documents/UniversityStuff/2021/Stat3007/STAT3007_Project/"

maleLocations = [github_path + "Audio_Speech_Actors_01-24/Male/"
             + x for x in 
             ["Actor_" + y + "/" for y in ["01", "03", "05", "07", "09", "11", "13", "15", "17", "19", "21", "23"]]]

femaleLocations = [github_path + "Audio_Speech_Actors_01-24/Female/"
             + x for x in 
             ["Actor_" + y + "/" for y in ["02", "04", "06", "08", "10", "12", "14", "16", "18", "20", "22", "24"]]]

locations = maleLocations + femaleLocations

big_file = open(github_path + "big_csv.csv", 'w')

big_file.write("Filenames,Emotion,Intensity,Phrase")
big_file.write("\n")


for location in locations:
    file = open(location + "targets" + location[-3] + location[-2] + ".txt", 'w')
    filenames = subprocess.check_output('ls -1 ' + location, shell=True, universal_newlines=True).split("\n")

    filenames.pop()
    filenames.pop()
    print(filenames)
    
    file.write("Filenames,Emotion,Intensity,Phrase")
    file.write("\n")
    
    for name in filenames:
        file.write(name + "," + name[1] + "," + name[4] + "," + name[7])
        file.write("\n")
        big_file.write(name + "," + name[1] + "," + name[4] + "," + name[7])
        big_file.write("\n")
    
    file.close()
big_file.close()
