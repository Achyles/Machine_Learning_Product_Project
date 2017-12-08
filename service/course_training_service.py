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
from filenames import *

def course_train(depart, modelname):
	#define the filename of saved model here
	fncmodel = modelname

	#load dictionaries of description and rating
	desDict = load_json(fndes, datapath)
	crDict = load_json(fncourse, datapath)

	#obtain the lists of keywords and corresponding rating
	wordList = list()
	scoreList = list()
	for key in crDict:
	    wordList.append(desDict[key][0])
	    scoreList.append(crDict[key])

	#train the model
	weModel = WE()
	weModel.train(wordList, scoreList)

	#save the model as dictionary to json file
	save_json(weModel.get_model(), fncmodel, modelpath)

if __name__ == "__main__":
	course_train(depart,mncourse)
