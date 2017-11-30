#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 23:02:08 2017

@author: Zixuan Li

A simple web scrapper for CU Course Directory.
Still in progress
"""

import requests
from bs4 import BeautifulSoup


def department_course_list(department):
    """
    Takes in a department four-letter abbreviation (e.g. COMS, STAT,IEOR)
    
    Return a list of strings of url for each course
    """
    
    courseURL = []
    site = requests.get("http://www.columbia.edu/cu/bulletin/uwb/subj/" + department + "/_Spring2018_text.html")
    siteBS = BeautifulSoup(site.content, "html.parser")
    
    for link in siteBS.find_all("a"):
        courseURL.append("http://www.columbia.edu" + link.get("href"))
    
    # The last one is for SIPA
    if courseURL[-1] == "http://www.columbia.edu/cu/sipa/COURSES/":
        return courseURL[:-1]
    else:
        return courseURL
    
    
    
    
    
    
    
    
##############################################################################
# Test Code Here
# COMS = requests.get("http://www.columbia.edu/cu/bulletin/uwb/sel/COMS_Spring2018.html")
# COMS_text= requests.get("http://www.columbia.edu/cu/bulletin/uwb/subj/COMS/_Spring2018_text.html")

# Get course listing part
# COMS_list = COMS_text.text.split("<pre>")[1].split("</pre>")[0]

# COMS_bs = BeautifulSoup(COMS.content, "html.parser")    
CS_course_URL = department_course_list("COMS")