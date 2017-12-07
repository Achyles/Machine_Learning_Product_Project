# -*- coding: utf-8 -*-
"""

@author: Achykes
"""

"""
This is an course evaluation service
based on pretrained models on course and prof reviews.
"""

import re
import pandas as pd
import json

input = 'COMS W1004 w4995'

modeln_c = 'course_model'
modeln_p = 'prof_model'

input = re.findall(r'\w+', input.upper())

depart = input[0]

courseData =  pd.read_csv('../data/'+depart+'_course_info.csv')

with open('../model/'+modeln_c+'.json') as fp1:
    cModel = json.load(fp1)
    
    
def get_descrip(depart, cnum, cData):
    

def predict(cnum):
        
    
    
    
print(cModel['code'])