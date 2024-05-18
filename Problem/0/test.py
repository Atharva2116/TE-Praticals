# Question1
# import webapp2

# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         self.response.write("Hello world")
        

# app=webapp2.WSGIApplication([('/',MainPage)],debug=True)  
     
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

# Question2

# import webapp2

# class Main(webapp2.RedirectHandler):
#     def get(self):
#         name = "Atharva"
#         seat_number = "123456789"
#         department = "IT Department"
        
#         for _ in range(5):
#             self.response.write("Name: {}<br>".format(name))
#             self.response.write("Seat Number: {}<br>".format(seat_number))
#             self.response.write("Department: {}<br>".format(department))
#             self.response.write("<br>")
            
# app=webapp2.WSGIApplication([('/',Main)],debug=True)


# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

# Question 3

# import webapp2

# class Main(webapp2.RedirectHandler):
#     def get(self):
#         seat_number = "123456789"
#         department = "IT Department"
        
#         counter=1
        
#         while(counter<11):
#             self.response.write(str(counter) + "<br>")
#             self.response.write("Seat Number: {}<br>".format(seat_number))
#             self.response.write("Department: {}<br>".format(department))
#             self.response.write("<br>") 
#             counter+=1
        
# app=webapp2.WSGIApplication([('/',Main)],debug=True)

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

# Question 4

# import webapp2

# class Main(webapp2.RedirectHandler):
#     def get(self):
#         self.response.write("Table of 5 <br>")
        
#         self.response.write("<ul>")
        
#         for i in range(1,11):
#             result=i*5
#             self.response.write("<li>{} X {} = {}</li>".format(5,i,result))
                
        
# app=webapp2.WSGIApplication([('/',Main)],debug=True)

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

# Question 5

# import webapp2

# class Main(webapp2.RedirectHandler):
#     def get(self):
#         self.response.write("Table of 5 <br>")
        
#         self.response.write("<ul>")
        
#         for i in range(1,11):
#             result=i*10
#             self.response.write("<li>{} X {} = {}</li>".format(10,i,result))
                
        
# app=webapp2.WSGIApplication([('/',Main)],debug=True)


# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

#Question 6

import webapp2

class Main(webapp2.RedirectHandler):
    def get(self):
        self.response.write("<h1>First 8 elements of Fibonacci series</h1>")
        fibonaic=[0,1]
        
        for i in range(2,8):
            next=fibonaic[-1]+fibonaic[-2]
            fibonaic.append(next)
        
        
        self.response.write("<ul>")
        for element in fibonaic:
            self.response.write("<li>{}</li>".format(element))
            
        self.response.write("</ul>")

app = webapp2.WSGIApplication([
    ('/', Main),
], debug=True)        
        
               