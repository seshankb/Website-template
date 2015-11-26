"""
 * ProjectBio v1.0 
 * Copyright 2014-2015 Web2all.
 * Licensed under Share2Create
 * Author: Senthilkumar M <allaboutsenthil.appspot.com>
 */
"""

import jinja2
import os
import webapp2
from datetime import datetime


TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))


class MainPage(BaseHandler):

    def get(self):
        self.render_template('index.html', {})


app = webapp2.WSGIApplication([
        ('/', MainPage)
        ],
        debug=True)
