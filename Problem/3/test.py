import webapp2

class MainHandler(webapp2.RedirectHandler):
    def get(self):
        seat_number="1234"
        department="IT"
        
        counter=0
        while counter<10:
            self.response.write(counter)
            self.response.write("<br>")
            self.response.write("Name: {}<br>".format(seat_number))
            self.response.write("Department :{}<br>".format(department))
            self.response.write("<br>")
            counter+=1
            
            
app=webapp2.WSGIApplication([('/',MainHandler),],debug=True)            