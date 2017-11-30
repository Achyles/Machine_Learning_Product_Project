#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 23:02:08 2017

@author: Zixuan Li

A simple web scrapper for CU Course Directory.
Still in progress
"""

import requests

COMS = requests.get("http://www.columbia.edu/cu/bulletin/uwb/sel/COMS_Spring2018.html")

COMS_text= requests.get("http://www.columbia.edu/cu/bulletin/uwb/subj/COMS/_Spring2018_text.html")

# Get course listing part
COMS_list = COMS_text.text.split("<pre>")[1].split("</pre>")[0]