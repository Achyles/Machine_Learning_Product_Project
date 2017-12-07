# -*- coding: utf-8 -*-
"""

@author: Achykes
"""

"""
This is an course evaluation service that
returns a score
based on pretrained models on course and prof reviews.
"""

import json
from filenames import *
	
	
def evaluate(depart, cnum):
	with open(modelpath+mncourse+'.json') as fp1:
		cModel = json.load(fp1)

	with open(modelpath+mnprof+'.json') as fp2:
		pModel = json.load(fp2)

	with open(datapath+fndes+'.json') as fp3:
		desDict = json.load(fp3)

	#Haven't implemented approximate rating for course not exists
	if cnum not in desDict:
		return 0

	ratingSum = 0
	wordList = desDict[cnum][0]

	for word in wordList:
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

if __name__ == "__main__":
	print(evaluate('COMS','W4995'))



