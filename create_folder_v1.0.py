#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  12 12:08:15 2022

@author: akshay kakar
"""

# This program creates a new folder with current date as its name

# suited for linux

from datetime import datetime
import os

# get today's date
today = datetime.now()

# create a directory or folder in Linux's "Documents" folder with today's date as its name
os.mkdir("/home/aki/Documents/" + today.strftime('%Y%m%d'))
os.mkdir("/home/aki/Documents/" + today.strftime('%Y%m%d') + '/' + 'folder_1')                                    # change folder name
os.mkdir("/home/aki/Documents/" + today.strftime('%Y%m%d') + '/' + 'folder_1' + '/' + 'folder_1_subfolder_1')     # change subfolder name
os.mkdir("/home/aki/Documents/" + today.strftime('%Y%m%d') + '/' + 'folder_1' + '/' + 'folder_1_subfolder_2')     # change subfolder name
