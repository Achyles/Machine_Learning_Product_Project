from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop 

import re
import sys
sys.path.append('../service')

from filenames import *	

class GetInfoHandler(RequestHandler):

	def set_default_headers(self):
		self.set_header('Access-Control-Allow-Credentials', 'true')
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "content-type, Authorization, Accept, X-Requested-With")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

	def get(self):
		self.write('This is the course get info api')

	def post(self):
		depart = self.get_argument('depart','none')
		cnums = self.get_argument('cnums','none')
		cnums = re.findall(r'\w+', cnums.upper())
		output = ''
		infoDict = load_json(fninfo, datapath)

		for cnum in cnums:
			info = infoDict[cnum]
			output += '<br />'+depart+' '+cnum+', '+info[0]+', <br />Professor: '+info[1]+'<br />'

		self.write(output)
	
if __name__ == "__main__":
		handler_mapping = [
							(r'/getinfo/', GetInfoHandler),
							]
		application = Application(handler_mapping)
		application.listen(7778)
		IOLoop.current().start()