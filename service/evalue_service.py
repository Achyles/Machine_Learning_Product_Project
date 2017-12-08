# -*- coding: utf-8 -*-
"""

@author: Achykes
"""

"""
This is an course evaluation service that
returns a score
based on pretrained models on course and prof reviews.
"""

import os.path
import pandas as pd
from filenames import *	
from make_data import *
	
def evaluate(depart, cnum):
	#check if data file exists
	if not os.path.isfile(modelpath+mncourse+'.json'):
		make_data()

	cModel = load_json(mncourse, modelpath)
	pModel = load_json(mnprof, modelpath)
	desDict = load_json(fndes, datapath)

	#Haven't implemented approximate rating for course not exists
	if cnum not in desDict:
		return 0

	ratingSum = 0
	rating = 0
	wordList = desDict[cnum][0]

	if len(wordList)==0:
		rating = 0
	else:
		for word in wordList:
			if word in cModel.keys():
				ratingSum += cModel[word][0]

		rating = ratingSum/len(wordList)

	match = 0

	profname = matchname(desDict[cnum][1], pModel.keys())

	if profname != 'none':
		rating = (rating+pModel[profname])/2

	return rating

def matchname(name1, nameList2):
	name1 = name1.lower().split()
	for name2 in nameList2:
		match = 0
		name2l = name2.lower()
		for name in name1:
			if name in name2l:
				match+=1
		if match>=2:
			return name2
	return 'none'

def get_info(cnums):
	infoDict = load_json(fninfo, datapath)
	res = ''
	for cnum in cnums:
		info = infoDict[cnum]
		res += '%6s%30s%s\n' % (cnum, info[0], info[1])
	return res

if __name__ == "__main__":
	print(evaluate('COMS','W4995'))
