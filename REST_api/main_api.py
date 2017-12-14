from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

from rank_api import *
from recommend_api import *
from review_api import *

"""
This is the main handler of CU Course Evaluation Service
"""

class MainHandler(RequestHandler):
	def set_default_headers(self):
		self.set_header('Access-Control-Allow-Credentials', 'true')
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "content-type, Authorization, Accept, X-Requested-With")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

	def options(self):
		self.set_status(204)
		self.finish()

if __name__ == "__main__":
		handler_mapping = [
							(r'/rank/', RankHandler),
							(r'/rec/', RecommandHandler),
							(r'/review/', ReviewHandler),
							]
		application = Application(handler_mapping)
		application.listen(7777)
		IOLoop.current().start()