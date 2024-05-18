import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        name = "Atharve"
        seat_number = "123456789"
        department = "IT Department"
        
        for _ in range(5):
            self.response.write("Name: {}<br>".format(name))
            self.response.write("Seat Number: {}<br>".format(seat_number))
            self.response.write("Department: {}<br>".format(department))
            self.response.write("<br>")  

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
