from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop 

import os.path
import pandas as pd

import sys
sys.path.append('../service')

from filenames import *	
from build_model import *


class EvalueHandler(RequestHandler):

	def set_default_headers(self):
		self.set_header('Access-Control-Allow-Credentials', 'true')
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "content-type, Authorization, Accept, X-Requested-With")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

	def get(self):
		self.write('This is the course evaluation api')

	def post(self):
		depart = self.get_argument('depart','none')
		cnum = self.get_argument('cnum','none')
		self.write(evaluate(depart, cnum))
		

def evaluate(depart, cnum):
	#check if data file exists
	if not os.path.isfile(modelpath+mncourse+'.json'):
		build_model(depart)

	cModel = load_json(mncourse, modelpath)
	pModel = load_json(mnprof, modelpath)
	desDict = load_json(depart+fndes, datapath)

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

	return str(rating)

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
		handler_mapping = [
							(r'/evalue/', EvalueHandler),
							]
		application = Application(handler_mapping)
		application.listen(7778)
		IOLoop.current().start()