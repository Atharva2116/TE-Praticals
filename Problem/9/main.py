import os
import webapp2
import urllib
import json
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'template/index.html')
        self.response.out.write(template.render(path, {}))

    def post(self):
        name = self.request.get('name')
        country = self.request.get('country')
        url = "http://universities.hipolabs.com/search?name={}&country={}".format(name, country)
        data = json.loads(urllib.urlopen(url).read())
        temp = {}
        path = 'template/error.html' if not data else 'template/result.html'
        temp["domains"] = data[0]['domains'][0] if data else None
        self.response.out.write(template.render(os.path.join(os.path.dirname(__file__), path), temp))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
