#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:46:39 2017

@author: Zixuan Li
"""
"""
from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from get_course_description import get


class ChartHandler1(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "content-type, Authorization, Accept, X-Requested-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Content-Type", "text/html/json; charset=UTF-8")

    def get(self,):
        data = get(["W1004"])
        self.write(data)


class ChartHandler2(tornado.web.RequestHandler):
    def set_default_headers(self):
        #self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "content-type, Authorization, Accept, X-Requested-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Content-Type", "text/html/json; charset=UTF-8")

    def post(self):
        data_json = self.request.arguments
        print(data_json)

if __name__ == "__main__":
    handler_mapping = [
                       (r'/chart1', ChartHandler1),
                       (r'/chart2', ChartHandler2)
                      ]
    application = tornado.web.Application(handler_mapping)
    application.listen(7777)
    tornado.ioloop.IOLoop.current().start()