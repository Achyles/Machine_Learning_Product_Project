# -*- coding: utf-8 -*-
"""

@author: Achykes
"""

"""
This service takes in professor rating data from Culpa to train the word embedding model.
The trained model is saved as a dictionary in json file.
"""

from embed_model import WordEmbed as WE
import pandas as pd

#define the department you working on here
depart = 'COMS'

#define the filename for saved model here
filename = 'prof_model'

#load culpa data
data =  pd.read_csv('../data/culpa.csv')

#preprocess the data
profr = data[['Professor','Rating']]
profr = profr.groupby(['Professor'])['Rating'].mean().to_dict()

#train the model
weModel = WE()
weModel.dict_train(profr)

#save the model to json file
weModel.save_model(filename)

