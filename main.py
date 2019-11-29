#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
  def get (self, q):
    if q is None:
      q = 'index.html'

    path = os.path.join (os.path.dirname (__file__), q)
    self.response.headers ['Content-Type'] = 'text/html'
    self.response.out.write (template.render (path, {}))

def main ():
  application = webapp.WSGIApplication ([('/(.*html)?', MainHandler)], debug=True)
  util.run_wsgi_app (application)



# Die folgende Zeile bewirkt, dass das Programm als Modul
# und als eigenstaendiges Programm verwendet werden kann
if __name__ == "__main__":
  main()

