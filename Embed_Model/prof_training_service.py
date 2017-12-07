# -*- coding: utf-8 -*-
"""

@author: Achykes
"""

"""
This is a model training service that
takes in professor rating data from Culpa to train the word embedding model.
The trained model is saved as a dictionary in json file.
"""

from embed_model import WordEmbed as WE
from filenames import *

def prof_train(depart, modelname):
	#define the filename of saved model here
	fnpmodel = depart+modelname

	#load dictionaries of professor rating
	profDict = load_json(fnprof, datapath)

	#train the model
	weModel = WE()
	weModel.train_dict(profDict)

	#save the model as dictionary to json file
	save_json(weModel.get_model(), fnpmodel, modelpath)

if __name__ == '__main__':
	prof_train(depart,mnprof)

