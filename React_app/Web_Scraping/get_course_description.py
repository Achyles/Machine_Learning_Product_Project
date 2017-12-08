#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:34:59 2017

@author: Zixuan Li

For usage of get function of the tornado API
"""

import csv

def get(ls, file = "./CU_Course_Directory_info/COMS_course_info.csv", unfound_warning = True):
    """
    Takes in a list of course numbers
    Return a dictionary of format {course number: course description}
    If there are multiple sections of the a course number,
    return description of the first section
    
    The function by default reads in the COMS course info,
    change it to other files by specifying the second argument.
    
    The function will print out a list of unfound courses,
    suppress this message by sepcifying the third argument.
    """
    
    all_course = {}
    
    with open(file, newline = "", encoding = "utf-8") as myfile:
        reader = csv.reader(myfile)
        for row in reader:
            if row[0] not in all_course.keys():
                all_course[row[0]] = row[6]
      
    selected = {}
    not_found = []
    for course in ls:
        if course in all_course.keys():
            selected[course] = all_course[course]
        else:
            not_found.append(course)        
            
    if unfound_warning and len(not_found) != 0:
        print("The following courses are not found: ", not_found)
        
    return selected
    
