# -*- coding: utf-8 -*-
"""

@author: Achyles
"""

"""
This is a model training service that
takes in culpa and CU course directory data to train the word embedding model.
The trained model is saved as a dictionary in json file.
"""

from embed_model import WordEmbed as WE
from preprocess import *

#define the filename of saved model here
fncmodel = depart+'_course_model'

#load dictionaries of description and rating
desDict = load_json(fndes, datapath)
crDict = load_json(fncourse, datapath)

#obtain the lists of keywords and corresponding rating
wordList = list()
scoreList = list()
for key in crDict:
    wordList.append(desDict[key])
    scoreList.append(crDict[key])

#train the model
weModel = WE()
weModel.train(wordList, scoreList)

#save the model as dictionary to json file
save_json(weModel.get_model(), fncmodel, modelpath)
