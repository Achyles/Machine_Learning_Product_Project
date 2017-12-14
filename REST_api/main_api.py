from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

from rank_api import *
from recommend_api import *
from review_api import *

"""
This is the main handler of CU Course Evaluation Service
"""

if __name__ == "__main__":
		handler_mapping = [
							(r'/rank/', RankHandler),
							(r'/rec/', RecommandHandler),
							(r'/review/', ReviewHandler),
							]
		application = Application(handler_mapping)
		application.listen(7777)
		IOLoop.current().start()