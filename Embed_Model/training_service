from embed_model import WordEmbed as WE
import pandas as pd
import re

data =  pd.read_csv('../data/culpa.csv')

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

cscore = pd.DataFrame(course,columns=['department','course number','rating'])

depart = 'COMS'
courseData =  pd.read_csv('../data/'+depart+'_course_info.csv')

score = cscore.loc[cscore['department'].isin([depart])]
score = score.groupby(['department','course number'])['rating'].mean().get(depart)
keys = score.keys()

desc = courseData[['course number','description']]

wordList = []
scoreList = []
for i in range(score.shape[0]):
    cnum = desc.at[i, 'course number']
    if cnum in keys:
        #obtain the keywords from description
        wordList.append(list(set(re.findall(r'\w+', desc.at[i, 'description'].lower()))))
        scoreList.append(score.get(cnum))

weModel = WE()
weModel.train(wordList, scoreList)
print(weModel.predict('in'))
