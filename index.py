import os.path
import random

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/edertgfdsawdssa5879654",JavaHandler),
            (r"/edertgfdsawdssa5879456",PythonHander)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html"
            # page_title = "Burt's Books | Home",
            # header_text = "Welcome to Burt's Books!",
        )

class JavaHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./java_url/Java.html")


class PythonHander(tornado.web.RequestHandler):
    def get(self):
        self.render("./python_url/Python.html")
if __name__ == '__main__':
    tornado.options.parse_command_line()
    # app = tornado.web.Application(
    #     handlers=[(r'/', IndexHandler)],
    #     template_path=os.path.join(os.path.dirname(__file__), "templates"),
    #     static_path=os.path.join(os.path.dirname(__file__), "static"),
    #     debug=True
    # )
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()