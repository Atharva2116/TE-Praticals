import webapp2
import os
import urllib
import json
from google.appengine.ext.webapp import template

class MainPage(webapp2.RedirectHandler):
    def get(self):
        self.response.out.write(template.render('templates/index.html',{}))
        
    def post(self):
        latitude = self.request.get('latitude')

        longitude=self.request.get('longitude')
        
        url = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&current_weather=true".format(latitude, longitude)
        data=json.loads(urllib.urlopen(url).read())
        
        template_values={}
        path='templates/error.html'
        
        if data.get("error") is None:
            temperature=data["current_weather"]["temperature"]
            windspeed=data["current_weather"]["windspeed"]
            template_values={"temperature":temperature,"windspeed":windspeed}
            path="templates/result.html"
            
        self.response.out.write(template.render(path,template_values))
        
app=webapp2.WSGIApplication([('/',MainPage),],debug=True)    
            