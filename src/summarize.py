#!/usr/bin/env python3

# This script summarizes the csv files in ../csv_files by merging all
# of the comment data into ../summary.csv
# This assumes that the Javascript code was run on posts all by the same
# TikTok account.
#
# To use:
# Run this script while there are csv files in ../csv_files generated
# by ScriptTikTokComments.py
#
# Output:
# A single csv file located at ../summary.csv



from os import path
import glob
  
# specifying the path to csv files
path = "../csv_files"
  
# csv files in the path
files = glob.glob(path + "/*.csv")

# creating empty list to hold the content from a csv
content = []

# checking all the csv files in the specified path
post_count = 0
comment_count = 0
for filename in files:
  # reading content of csv file
  with open(filename,'r', newline='') as csvfile:
    clean_lines = []
    all_lines = csvfile.readlines()
    # removing newlines and single quotes. prob not needed
    for line in all_lines:      
      line = line.rstrip('\n').replace('\'\"','')
      clean_lines.append(line)
    # saving header and post url on first iteration
    if post_count == 0:
      csv_header = clean_lines[14] + ",Post URL"
      # first line of the final content list should be header
      content.append(csv_header)
      post_url = clean_lines[1][9:]
    # skipping post info/header
    line_count = 15
    # grabbing comment data for this file
    # and adding the post_url to the end of each row
    for clean_line in clean_lines[15:]:
      clean_line += ",{}".format(post_url)
      clean_lines[line_count] = clean_line
      line_count += 1
    content.extend(clean_lines[15:])
    comment_count += len(clean_lines[15:])
  post_count += 1

content = [each_line + '\n' for each_line in content]

with open("../summary.csv",'w', newline='') as s:
  s.writelines(content)

print("\n\x1b[32m[*]\x1b[0m Done scraping {} post(s) for {} comment(s).".format(post_count, comment_count), end="\n\n")
