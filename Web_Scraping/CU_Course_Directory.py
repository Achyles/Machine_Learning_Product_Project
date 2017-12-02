#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 23:02:08 2017

@author: Zixuan Li

A simple web scraper for CU Course Directory for Spring 2018 Courses
Can be modified for other terms as well
Usage sample, from terminal run:
    python CU_Course_Directory.py 
    COMS STAT IEOR -d out/
"""

import requests
from bs4 import BeautifulSoup
import re
import csv
import os


def department_course_list(department):
    """
    Takes in a department four-letter abbreviation (e.g. COMS, STAT,IEOR)
    
    Return a list of strings of url for each course
    """
    
    courseURL = []
    site = requests.get("http://www.columbia.edu/cu/bulletin/uwb/subj/" + department + "/_Spring2018_text.html")
    siteBS = BeautifulSoup(site.content, "lxml")
    
    for link in siteBS.find_all("a"):
        courseURL.append("http://www.columbia.edu" + link.get("href"))
    
    # The last one is for SIPA
    if courseURL[-1] == "http://www.columbia.edu/cu/sipa/COURSES/":
        return courseURL[:-1]
    else:
        return courseURL
    
def course_info(course_list):
    """
    Takes in a course list of urls
    
    Return a dict of course information
    The key of the dict is a tuple of (course number, section number)
    The value of the dict is another dict containing info of "course number",
    "section","name", "description", "instructor", "instructor 2", "is full"
    
    A message will be printed out if there is some request cannot be made
    """
    
    courseDict = {}
    
    for link in course_list:
        try:        
            
            course = requests.get(link)
            courseBS = BeautifulSoup(course.content, "lxml")
            
            s = courseBS.get_text()
            ls = re.split("\n+", s)
            
            try:
                course_description_ixs = ls.index("Course Description") + 1
            except:
                course_description_ixs = -1
            course_description_ixe = ls.index("Web Site") - 1
            
            try:
                multi_ins = False
                instructor_ix = ls.index("Instructor") + 1
                if ls[instructor_ix] == "Instructor":
                    instructor_ix += 1
            except:
                try:
                    multi_ins = True
                    instructor_ix = ls.index("Instructors") + 1
                except:
                    instructor_ix = -1
           
            name_ix = ls.index("Call Number") - 1
            number_ix = ls.index("Number") + 1
            section_ix = ls.index("Section") + 1        
            try:
                status_ix = ls.index("Status") + 1
            except:
                status_ix = -1
            
            key = (ls[number_ix], ls[section_ix])
            courseDict[key] = {}
            courseDict[key]["course number"] = ls[number_ix]
            courseDict[key]["section"] = ls[section_ix]
            courseDict[key]["name"] = ls[name_ix]
            courseDict[key]["description"] = ""
            
            while course_description_ixs <= course_description_ixe and course_description_ixs != -1:
                courseDict[key]["description"] += ls[course_description_ixs]
                course_description_ixs += 1
            
            if instructor_ix == -1:
                courseDict[key]["instructor"] = ""
            else:
                courseDict[key]["instructor"] = ls[instructor_ix]                
                courseDict[key]["instructor 2"] = ""
                if multi_ins:
                    courseDict[key]["instructor 2"] = ls[instructor_ix+1]
            
            if status_ix == -1:
                courseDict[key]["is full"] = "false"
            else:
                courseDict[key]["is full"] = "true"
                
            ## print("Request: "+ link + ": Succeed.")
        except:
            print("Request: "+ link + ": Fail!")
            print("You may check the site maually, or edit the code.")
            continue
            
    return courseDict
        
def write_csv(course_dict, file_name, directory = ""):
    """
    Takes in a course dict, a file name, directory
    
    Writes a csv file of the course infomation to a given directory.
    The default directory is current directory.
    """
    directory = "./" + directory
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file = open(directory+file_name, "w")
    
    with file:
        fields = ["course number","section","name", "instructor", "instructor 2", "is full", "description"]
        
        writer = csv.DictWriter(file, fieldnames=fields)
        
        writer.writeheader()
        
        for course in course_dict:
            writer.writerow(course_dict[course])
            
    print("Finish writing " + file_name)
    

if __name__ == "__main__":
    ls = input("Please enter a list of four-letter department abbreviations (e.g. COMS, HIST, MATH) to get csv files of course information.\nFiles will be stored by default in the current directory, you can also change the directory with \"-d\" flag + directory: \n")
    ls = ls.split(" ")
    directory = ""
    for item in ls:
        if item == "-d":
            try:
                rem = ls[ls.index(item)+1]
                directory += ls[ls.index(item)+1]
            except:
                print("Please format the input correctly")
        
            ls.remove("-d")
            ls.remove(rem)
                
    for course in ls:        
        if len(course) == 4:
            cls = department_course_list(course)
            cd = course_info(cls)
            write_csv(cd, course + "_course_info.csv", directory) 
    
    
    
    
    
##############################################################################
# Test Code Here    
# COMS = requests.get("http://www.columbia.edu/cu/bulletin/uwb/sel/COMS_Spring2018.html")
# COMS_text= requests.get("http://www.columbia.edu/cu/bulletin/uwb/subj/COMS/_Spring2018_text.html")

# Get course listing part
# COMS_list = COMS_text.text.split("<pre>")[1].split("</pre>")[0]

# COMS_bs = BeautifulSoup(COMS.content, "html.parser")    
#CS_course_URL = department_course_list("COMS")
#
#
#W1004 = requests.get("http://www.columbia.edu/cu/bulletin/uwb/subj/COMS/W1004-20181-001/")
#
#soup = BeautifulSoup(W1004.content, "lxml")
#meta = soup.find_all("meta")
#type(meta[1].get("content"))
#
#E6998 = requests.get("http://www.columbia.edu/cu/bulletin/uwb/subj/COMS/E6998-20181-012/")
#soup2 = BeautifulSoup(E6998.content, "lxml")
    
