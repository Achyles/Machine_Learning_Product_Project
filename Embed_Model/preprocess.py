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
import json
import os

#define the department you working on here
depart = 'COMS'

#define the filenames here
fndes = depart+'_'+'des_dict'
fncourse = depart+'_'+'course_dict'
fnprof = 'prof_dict'

#define path here
datapath = '../data/'
modelpath = '../model/'


#save input object to json file
#create directory if not exist
def save_json(myob, filename, path):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path+filename+'.json','w') as fp:
        json.dump(myob, fp)

#load and return the object from json file        
def load_json(filename, path):
    with open(path+filename+'.json') as fp:
        return json.load(fp)        


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
desc = courseData[['course number','description']]
keys = crating.keys()
desDict = dict()
crDict = dict()

#match the description corpus with the rating score for each course 
#and store in a dictionary
for i in range(desc.shape[0]):    
    cnum = desc.at[i, 'course number']    
    
    #obtain the keywords from description and its score
    des = desc.at[i, 'description']
    if not isinstance(des, str):
        continue
        
    wlist = list(set(re.findall(r'\w+', des.lower())))
    
    #store the course number corresponding keywords in dictionary
    desDict.update({cnum:wlist})
    
    #store the course number corresponding ratings in dictionary
    if cnum in keys:  
        crDict.update({cnum:crating.get(cnum)})

        
#save the dictionaries to json files
save_json(desDict, fndes, datapath)
save_json(crDict, fncourse, datapath)
save_json(profDict, fnprof, datapath)





