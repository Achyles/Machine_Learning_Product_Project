from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop 

import sys
sys.path.append('../service')

from rank_service import *

"""
ranking service for input department and course numbers
e.g.:
localhost:7777/?rank=COMS+W4111+w1004+w4995

"""

class RankHandler(RequestHandler):
	def get(self):
		input = self.get_argument('rank','none')

		self.write(rank_course(input))

"""	def post(self):
		input = self.get_argument('rank','none')
		self.write(rank_course(input))"""

if __name__ == "__main__":
		handler_mapping = [
							(r'/', RankHandler),
						    ]
		application = Application(handler_mapping)
		application.listen(7777)
		IOLoop.current().start()
