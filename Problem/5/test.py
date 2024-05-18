import webapp2

class MainHandler(webapp2.RedirectHandler):
    def get(self):
        self.response.write("<h1>Table of 10</h1>")
        self.response.write("<ul>")
        
        for i in range(1,11):
            result=i*10
            
            self.response.write("<li>{} x {} = {} </li>".format(10,i,result))
            
        self.response.write("</ul>") 
        
app=webapp2.WSGIApplication([('/',MainHandler)],debug=True)           