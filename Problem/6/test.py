import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("<h1>First 8 elements of Fibonacci series</h1>")
        fibonacci_series=[0,1]
        
        for i in range(2,8):
            next_element=fibonacci_series[-1]+fibonacci_series[-2]
            fibonacci_series.append(next_element)
            
        self.response.write("<ul>")
        for element in fibonacci_series:
            self.response.write("<li>{}</li>".format(element)) 
        self.response.write("</ul>")
   
   
app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)        
        
               