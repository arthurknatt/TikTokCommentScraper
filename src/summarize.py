#!/usr/bin/env python3

from distutils.command import clean
import sys
from csv import reader, writer, QUOTE_ALL, QUOTE_NONE
from os import system, getcwd, remove, path, rename
from datetime import datetime as d
from pyperclip import paste, PyperclipException
from openpyxl import Workbook

# importing the required modules
import glob
  
# specifying the path to csv files
path = "../csv_files"
  
# csv files in the path
files = glob.glob(path + "/*.csv")

# creating empty list to hold the content from a csv
content = []

# checking all the csv files in the 
# specified path
post_count = 0
comment_count = 0
for filename in files:
  # reading content of csv file
  with open(filename,'r', newline='') as csvfile:
    clean_lines = []
    all_lines = csvfile.readlines()
    # removing newlines and single quotes. prob not needed
    for line in all_lines:      
      actual_line = line.rstrip('\n').replace('\'\"','')
      clean_lines.append(actual_line)
    # saving header and post url on first iteration
    if post_count == 0:
      csv_header = clean_lines[14] + ",Post URL"
      content.append(csv_header)
    post_url = clean_lines[1][9:]
    # skipping post info/header
    count = 15
    for clean_line in clean_lines[15:]:
      clean_line += ",{}".format(post_url)
      clean_lines[count] = clean_line
      count += 1
    content.extend(clean_lines[15:])
    comment_count += len(clean_lines[15:])
  post_count += 1

content = [each_line + '\n' for each_line in content]

with open("../summary.csv",'w', newline='') as s:
  s.writelines(content)

print("\n\x1b[32m[*]\x1b[0m Done scraping {} post(s) for {} comment(s).".format(post_count, comment_count), end="\n\n")
