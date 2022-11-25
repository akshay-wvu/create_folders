#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  12 16:03:48 2022

@author: akshay kakar
"""

# This program creates a new folder with current date as its name

from datetime import datetime
import time
import os


# final execution of directory/folder creation
# function for importing the folder name and location information
def create_todays_folder(initialized_folder_location, insert_folder_name,
                         insert_force_displacement, insert_stress_strain,
                         insert_resistance_strain, insert_norm_resistance_strain,
                         insert_sem, insert_thermocouple,
                         insert_python_codes, insert_solidworks_designs,
                         insert_image_analysis, insert_raw_images,
                         insert_edited_images):

    # create the directory/folder based on the set location and name in the main function
    os.mkdir(initialized_folder_location + insert_folder_name)
    main_folder = initialized_folder_location + insert_folder_name + "/"

    # Show main folder path
    print("Main folder:\n", main_folder, "\n")

    # sub-folders inside the main folder
    os.mkdir(main_folder + insert_force_displacement)      # F vs Disp folder
    os.mkdir(main_folder + insert_stress_strain)           # Stress vs Strain folder
    os.mkdir(main_folder + insert_resistance_strain)       # R vs Strain folder
    os.mkdir(main_folder + insert_norm_resistance_strain)  # Norm R vs Strain folder
    os.mkdir(main_folder + insert_sem)                     # SEM folder
    os.mkdir(main_folder + insert_thermocouple)            # Thermocouple folder
    os.mkdir(main_folder + insert_python_codes)            # Python Codes folder
    os.mkdir(main_folder + insert_solidworks_designs)      # SolidWorks Designs folder
    os.mkdir(main_folder + insert_image_analysis)          # Image Analysis folder

    # sub-folders for Image Analysis folder
    image_analysis_folder = main_folder + insert_image_analysis + "/"
    os.mkdir(image_analysis_folder + insert_raw_images)     # Raw Images folder
    os.mkdir(image_analysis_folder + insert_edited_images)     # Edited Images folder

    # Show sub-folder paths
    print("Sub-folders:\n", main_folder + insert_force_displacement, "\n", main_folder + insert_stress_strain, "\n",
          main_folder + insert_resistance_strain, "\n", main_folder + insert_norm_resistance_strain, "\n",
          main_folder + insert_sem, "\n", main_folder + insert_thermocouple, "\n",
          main_folder + insert_python_codes, "\n", main_folder + insert_solidworks_designs, "\n",
          main_folder + insert_image_analysis, "\n", image_analysis_folder + insert_raw_images, "\n",
          image_analysis_folder + insert_edited_images, "\n")

    print("Successful!\n")


# main function where all variables and values are initialized
def main():
    # get current date and time
    date_time = datetime.now()
    print("\nCurrent date and time: ", date_time)

    # initialize folder location (suited for Linux)
    folder_location = "/home/akshay/Documents/"
    print("Folder location: ", folder_location, "\n")

    # initialize folder location (suited for Windows)
    """folder_location = "C:/Users/Akshay/Documents/"
    """

    # initialize folder's name to today's date in the format YYYYMMDD
    folder_name = date_time.strftime('%Y%m%d')

    # initialize names for other folders
    force_displacement = "F vs Disp"
    stress_strain = "Stress vs Strain"
    resistance_strain = "R vs Strain"
    norm_resistance_strain = "Norm R vs Strain"
    sem = "SEM"
    thermocouple = "Thermocouple"
    python_codes = "Python Codes"
    solidworks_designs = "SolidWorks Designs"
    image_analysis = "Image Analysis"
    raw_images = "Raw Images"
    edited_images = "Edited Images"

    # call function to create today's folder
    create_todays_folder(folder_location, folder_name, force_displacement,
                         stress_strain, resistance_strain,
                         norm_resistance_strain, sem,
                         thermocouple, python_codes,
                         solidworks_designs, image_analysis,
                         raw_images, edited_images)


# checks if the main function is required to be executed
if __name__ == '__main__':
    # info to be displayed for user before the program runs or shows an error
    print("This is the main program, which runs only for the first time.")
    time.sleep(3)  # gives user 3 seconds to read

    print("It creates a new folder with current date as its name.")
    time.sleep(3)  # gives user 3 seconds to read

    print("If this folder already exists, you will see an ERROR below.\n")
    time.sleep(5)  # gives user 5 seconds to read error warning

    # ask user if they want to proceed
    go_ahead = input("Would you like to continue? (Y/n)\n")
    # capitalize user input to make the following if statement simpler
    capitalize_go_ahead = go_ahead.capitalize()

    if capitalize_go_ahead == "Y":
        main()
    else:
        print("Program exited.\n\nHave a good one!")
        exit()

# shortened code for the entire program is commented below (suited for linux)
"""
from datetime import datetime
import os

# get today's date
today = datetime.now()

# create a directory or folder in Linux's "Documents" folder with today's date as its name
os.mkdir("/home/aki/Documents/" + today.strftime('%Y%m%d'))
"""
