import jinja2
import logging
import os
import webapp2
import json

from google.appengine.ext import ndb
from google.appengine.api import users

# Main page setup
class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

# Jinja setup
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Application setup
application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
