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
        self.response.out.write(template.render({'login': users.create_login_url('/app')}))

# Serve the app
class AppPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('app.html')
        self.response.out.write(template.render({
            'user': users.get_current_user().nickname(),
            'logout': users.create_logout_url('/')
        }))

# Jinja setup
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Application setup
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/app', AppPage)
], debug=True)
