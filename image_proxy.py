#/use/local/bin/python3

import os.path

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

from app.HomeHandler import HomeHandler
from app.ImageProxyHandler import ImageProxyHandler
from app.AuthHandlers import AuthLoginHandler, AuthLogoutHandler

class Application(tornado.web.Application):
  def __init__(self):
    handlers = [
        (r"/", HomeHandler),
        (r"/image", ImageProxyHandler),
        ]
    settings = dict(
        cookie_secret="aowuhdoqu3ahrOfQUHDr08e0a8dh202h0odiaej",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True,
        login_url="/auth/login",
        )
    tornado.web.Application.__init__(self, handlers, **settings)


def main():
  tornado.options.parse_command_line()
  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
  main()

