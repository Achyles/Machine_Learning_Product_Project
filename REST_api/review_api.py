from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

import sys

sys.path.append('../service')

from review_service import *

"""
ranking service for input department and course numbers
e.g.:
localhost:7777/review/?review=COMS+W4111+w1004+w4995
"""


class ReviewHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "content-type, Authorization, Accept, X-Requested-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        # take professor + course_number input
        # e.g.: 'COMS w4111 w4995 w4170'
        input = self.get_argument('review', 'none')
        input = input.replace(",", "").split()
        l_name = input[0].lower()
        f_name = input[1].lower()
        course = input[2]
        output, course_name, course_num, review_num = review_course(l_name, f_name, course)
        course_num = course_num.replace(']', '').replace('[','').strip()
        l_name = l_name[0].upper() + l_name[1:]
        f_name = f_name[0].upper() + f_name[1:]
        if not output :
            self.write("<h3>We do not have matching data. Please check your input.<h3>")
        else:
            self.write('<h3>{} by Professor {} </h3>'.format(course_num + ': ' + course_name, f_name + ' ' + l_name))
            self.write('<h3>Total of {} reviews are submitted for your query.</h3>'.format(review_num))
            for review in output:
                self.write('<h4>{}</h4  >'.format(review))

        # self.write(input)
    def options(self):
        self.set_status(204)
        self.finish()


"""	def post(self):
		input = self.get_argument('rank','none')
		self.write(rank_course(input))"""

if __name__ == "__main__":
    handler_mapping = [
        (r'/review/', ReviewHandler),
    ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()