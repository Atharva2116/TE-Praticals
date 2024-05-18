import webapp2
class Page(webapp2.RedirectHandler):
    def get(self):
        self.response.write("Hello world")

app=webapp2.WSGIApplication([('/',Page)],debug=True)        