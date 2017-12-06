# -*- coding: utf-8 -*-
"""

@author: Achyles
"""

"""
This service takes in culpa and CU course directory data to train the word embedding model.
The trained model is saved as a dictionary in json file.
"""

from embed_model import WordEmbed as WE
import pandas as pd
import re

#define the department you working on here
depart = 'COMS'

#define the filename for saved model here
filename = 'course_model'

#load data
data =  pd.read_csv('../data/culpa.csv')
courseData =  pd.read_csv('../data/'+depart+'_course_info.csv')


#cleaning culpa data
cr = data[['Course','Rating']]
course = []

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

#preprocess culpa data
cscore = pd.DataFrame(course,columns=['department','course number','rating'])
score = cscore.loc[cscore['department'].isin([depart])]
score = score.groupby(['department','course number'])['rating'].mean().get(depart)
keys = score.keys()


#preprocess directory data
desc = courseData[['course number','description']]
wordList = []
scoreList = []

#matching the description corpus with the rating score
#stored in wordList and scoreList with indices matching
for i in range(score.shape[0]):
    cnum = desc.at[i, 'course number']
    if cnum in keys:
        #obtain the keywords from description
        wordList.append(list(set(re.findall(r'\w+', desc.at[i, 'description'].lower()))))
        scoreList.append(score.get(cnum))


#train the model
weModel = WE()
weModel.train(wordList, scoreList)

#save the model as dictionary to json file
weModel.save_model(filename)