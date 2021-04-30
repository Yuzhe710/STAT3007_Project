#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:33:13 2021

@author: jordan
"""

import subprocess
noise_names = ["AirConditioner_1","AirConditioner_10","AirConditioner_2","AirConditioner_3","AirConditioner_4","AirConditioner_5","AirConditioner_6","AirConditioner_7","AirConditioner_8","AirConditioner_9","AirportAnnouncement_11","AirportAnnouncements_1","AirportAnnouncements_10","AirportAnnouncements_2","AirportAnnouncements_3","AirportAnnouncements_4","AirportAnnouncements_5","AirportAnnouncements_6","AirportAnnouncements_7","AirportAnnouncements_8","AirportAnnouncements_9","Babble_1","Babble_10","Babble_11","Babble_12","Babble_2","Babble_3","Babble_4","Babble_5","Babble_6","Babble_7","Babble_8","Babble_9","Bus_1","CafeTeria_1","Cafe_1","Car_1","CopyMachine_1","CopyMachine_10","CopyMachine_2","CopyMachine_3","CopyMachine_4","CopyMachine_5","CopyMachine_6","CopyMachine_7","CopyMachine_8","Field_1","Hallway_1","Kitchen_1","LivingRoom_1","Metro_1","Munching_1","Munching_10","Munching_2","Munching_3","Munching_4","Munching_6","Munching_7","Munching_8","Munching_9","NeighborSpeaking_1","NeighborSpeaking_10","NeighborSpeaking_11","NeighborSpeaking_12","NeighborSpeaking_13","NeighborSpeaking_14","NeighborSpeaking_2","NeighborSpeaking_3","NeighborSpeaking_4","NeighborSpeaking_5","NeighborSpeaking_6","NeighborSpeaking_7","NeighborSpeaking_8","NeighborSpeaking_9","Office_1","Park_1","Restaurant_1","ShuttingDoor_1","ShuttingDoor_10","ShuttingDoor_2","ShuttingDoor_3","ShuttingDoor_4","ShuttingDoor_5","ShuttingDoor_6","ShuttingDoor_7","ShuttingDoor_8","ShuttingDoor_9","Square_1","SqueakyChair_1","SqueakyChair_10","SqueakyChair_11","SqueakyChair_2","SqueakyChair_3","SqueakyChair_4","SqueakyChair_5","SqueakyChair_6","SqueakyChair_7","SqueakyChair_8","SqueakyChair_9","Station_1","Traffic_1","Typing_1","Typing_10","Typing_2","Typing_3","Typing_4","Typing_5","Typing_6","Typing_7","Typing_8","Typing_9","VacuumCleaner_1","VacuumCleaner_2","VacuumCleaner_3","VacuumCleaner_4","VacuumCleaner_5","VacuumCleaner_6","VacuumCleaner_7","VacuumCleaner_8","VacuumCleaner_9","WasherDryer_1","WasherDryer_2","WasherDryer_3","WasherDryer_4","WasherDryer_5","WasherDryer_6","WasherDryer_7","Washing_1"]

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
    file = open(location + "targets" + location[-3] + location[-2] + ".csv", 'w')
    filenames = subprocess.check_output('ls -1 ' + location, shell=True, universal_newlines=True).split("\n")

    filenames.pop()
    filenames.pop()
    
    file.write("Filenames,Emotion,Intensity,Phrase")
    file.write("\n")
    
    for name in filenames:
        file.write(name + "," + name[1] + "," + name[4] + "," + name[7])
        file.write("\n")
        for noise_name in noise_names:
            name_without_wav = name[:len(name)-4]
            big_file.write(name_without_wav + "_" + noise_name + ".wav" + "," + name[1] + "," + name[4] + "," + name[7])
            big_file.write("\n")
    
    file.close()
big_file.close()
