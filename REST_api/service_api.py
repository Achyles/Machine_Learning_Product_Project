from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

from evalue_api import *
from get_info_api import *

if __name__ == "__main__":

		handler_mapping = [
							(r'/evalue/', EvalueHandler),
							(r'/getinfo/', GetInfoHandler)
							]
		application = Application(handler_mapping)
		application.listen(7778)
		IOLoop.current().start()