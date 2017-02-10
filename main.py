import jinja2
import logging
import os
import webapp2
import json

from google.appengine.ext import ndb
from google.appengine.api import users

# A Rotterdammer has a user ID and a number of credits
class Rotterdammer(ndb.Model):
    user_id = ndb.StringProperty()
    credits = ndb.IntegerProperty()

    @classmethod
    def get_by_user(cls, user):
        return cls.query().filter(cls.user_id == user.user_id()).get()

# Main page setup
class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render({'login': users.create_login_url('/app')}))

# Serve the app
class AppPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('app.html')

        user = users.get_current_user()
        rotterdammer = Rotterdammer.get_by_user(user)

        if rotterdammer is not None:
            credits = rotterdammer.credits
        else:
            credits = 0

        self.response.out.write(template.render({
            'user': user.email(),
            'credits': credits,
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
