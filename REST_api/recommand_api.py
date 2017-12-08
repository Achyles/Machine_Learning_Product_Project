from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop 

import sys
sys.path.append('../service')

from rank_service import *
from recommand_service import *

"""
ranking service for input department and course numbers
e.g.:
localhost:7777/rec/?rec=COMS
"""

class RecommandHandler(RequestHandler):
	#take department input e.g.: 'COMS'
	def get(self):
		input = self.get_argument('rec','none')

		self.write(recommand_course(input))


if __name__ == "__main__":
		handler_mapping = [
							(r'/rec/', RecommandHandler),
							]
		application = Application(handler_mapping)
		application.listen(7777)
		IOLoop.current().start()