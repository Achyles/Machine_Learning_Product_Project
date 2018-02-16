from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop 

import requests

import sys
sys.path.append('../service')

from filenames import *

"""
ranking service for input department and course numbers
e.g.:
localhost:7777/rec/?rec=COMS
"""

class RecommendHandler(RequestHandler):
	def set_default_headers(self):
		self.set_header('Access-Control-Allow-Credentials', 'true')
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "content-type, Authorization, Accept, X-Requested-With")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

	#take department input e.g.: 'COMS'
	def get(self):
		
		input = self.get_argument('rec','none')

		self.write(recommand_course(input))

def recommand_course(depart):

	desDict = load_json(depart+fndes, datapath)

	scoreDict = {}

	for cnum in desDict.keys():
		
		score = requests.post(url = 'http://localhost:7778/evalue/', data = {'depart':depart, 'cnum':cnum})
		scoreDict.update({cnum:float(score.text)})

	top10 = sorted(scoreDict, key=scoreDict.get, reverse=True)[:10]
	
	rankinfo = requests.post(url = 'http://localhost:7778/getinfo/', data = {'depart':depart, 'cnums':' '.join(top10)})

	return rankinfo.text


if __name__ == "__main__":
		handler_mapping = [
							(r'/rec/', RecommendHandler),
							]
		application = Application(handler_mapping)
		application.listen(7777)
		IOLoop.current().start()
