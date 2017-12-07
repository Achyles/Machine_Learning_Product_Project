#define the department you working on here
depart = 'COMS'

#define the filenames for dictionaries

fndes = depart+'_'+'des_dict'
fncourse = depart+'_'+'course_dict'
fnprof = 'prof_dict'

#define the filenames for models
mncourse = 'course_model'
mnprof = 'prof_model'

#define path here
datapath = '../data/'
modelpath = '../model/'

import json
import os

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