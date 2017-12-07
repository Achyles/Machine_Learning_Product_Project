#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:46:39 2017

@author: Zixuan Li
"""

from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

from get_course_description import get


class ChartHandler(RequestHandler):
    def set_default_headers(self):
        super(ChartHandler, self).set_default_headers()
        self.set_header('Access-Control-Allow-Origin', 'http://localhost:3000')
        self.set_header('Access-Control-Allow-Credentials', 'true')

    def get(self, chart_name):
        data = get(["W1004","W3157","W4118"])
        self.write(data)

if __name__ == "__main__":
    handler_mapping = [
                       (r'/chart/([a-zA-Z]+)$', ChartHandler),
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()