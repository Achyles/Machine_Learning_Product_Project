# -*- coding: utf-8 -*-
"""

@author: Achykes
"""

"""
Preprocessing on raw data.
Output dictionaries of course/prof description/rating in json files/
"""

import pandas as pd
import re
from filenames import *   

def preprocess(depart):
    #load data
    culpaData =  pd.read_csv('../data/culpa.csv')
    courseData =  pd.read_csv('../data/'+depart+'_course_info.csv')

    #preprocess culpa course data
    cr = culpaData[['Course','Rating']]
    course = []

    #formatting invalid course number
    for i in range(cr.shape[0]):
        
        s = cr.at[i,'Course'].split()
        
        #skip 'none' or course number without department
        if len(s)<2:
            continue

        #formatting course number
        if s[1][0].isdigit():
            if s[1][0]=='6':
                s[1] = 'E'+s[1]
            else:
                s[1] = 'W'+s[1]
        
        course.append([s[0].upper(),s[1],cr.at[i,'Rating']])

    #save the rating of each course to a dictionary with key:['depart', 'course_number']
    crating = pd.DataFrame(course,columns=['department','course number','rating'])
    crating = crating.groupby(['department','course number'])['rating'].mean().get(depart)

    #save the rating of each professor to a dictionary with key:['professor_name']
    profr = culpaData[['Professor','Rating']]
    profDict = profr.groupby(['Professor'])['Rating'].mean().to_dict()


    #preprocess CU directory data
    desc = courseData[['course number','name','instructor','description']]
    keys = crating.keys()
    desDict = dict()
    crDict = dict()
    infoDict = dict()

    #match the description corpus with the rating score for each course 
    #and store in a dictionary
    for i in range(desc.shape[0]):    
        cnum = desc.at[i, 'course number']    
        
        #save course info to infoDict
        infoDict.update({cnum:[desc.at[i, 'name'],
                                desc.at[i, 'instructor']]})

        #obtain the keywords from description and its score
        des = desc.at[i, 'description']
        wlist = list()
        if not isinstance(des, str):
            wlist = []
        else:
            wlist = list(set(re.findall(r'\w+', des.lower())))
        
        #store the course number corresponding keywords in dictionary
        desDict.update({cnum:[wlist,desc.at[i, 'instructor']]})
        
        #store the course number corresponding ratings in dictionary
        if cnum in keys:  
            crDict.update({cnum:crating.get(cnum)})

            
    #save the dictionaries to json files
    global fndes
    global fncourse
    fndes = depart+'_'+'des_dict'
    fncourse = depart+'_'+'course_dict'
    
    save_json(desDict, fndes, datapath)
    save_json(crDict, fncourse, datapath)
    save_json(profDict, fnprof, datapath)
    save_json(infoDict, fninfo, datapath)

if __name__ == "__main__":
    preprocess('COMS')



