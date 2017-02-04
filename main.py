#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

form = """
<h1>User Signup</h1>
<form method = "post">
<table>
<tr>
<td>
<label>Username: <input type="text" name="username"/></label>
</td>
<td>
<label style="color:red">{username_message}</label>
</td>
</tr>
    
<tr>
<td>
<label>Password: <input type="text" name="password"/></label>
<td>
<label>{password_message}</label>
</td>
</td></tr>
    
<tr>
<td>
<label>Verify Password: <input type="text" name="verify_password"/></label>
<td> 
<label>{password_match_message}</label>
</td>
</td></tr>
    
<tr>
<td>
<label>Email (optional): <input type="text" name="email"/></label>
<td>
<label>{email_message}</label>
</td>
</td></tr>
    
</table>
<input type = 'submit'/>
</form>
"""            
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

def equal_password(verify_password, password):
    if password == verify_password:
        return True
    else: 
        return False

EMAIL_RE = re.compile(r'^[\S]+@[\S\+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)


        
class MainHandler(webapp2.RequestHandler):
    def helper(self, user_message="", user_password="", match_password="", user_email=""):
       self.response.write(form.format(username_message= user_message, 
                                  password_message= user_password, 
                                  password_match_message= match_password,
                                  email_message= user_email
                                  ))
             
    def get(self):
        self.helper()        
        
    def post(self):
        # look inside the request to figure out what the user typed
        username = self.request.get("username")
        password = self.request.get("password")
        verify_password = self.request.get("verify_password")
        email = self.request.get("email")
        #user_message = self.request.get("username_message")
        #user_password = self.request.get("password_message")
        #match_password = self.request.get("password_match_message")
        #user_email = self.request.get("email_message")
        
        params = dict(username = username,
                      email = email)
        
        # if the user doesn't type anytying
        #if valid_username(username) == "" or ! valid_username
        user_message="" 
        user_password=""
        match_password=""
        user_email=""
        if valid_username(username) and valid_password(password) and equal_password(password, verify_password) and valid_email(email):
            self.redirect('/welcome?username=' + username)
        if not valid_username(username):
            user_message="Username not valid"
        if not valid_password(password):
            user_password="Password not valid"
        if not equal_password(password, verify_password):
            match_password="Passwords must match"
        if email is not "" and not valid_email(email):
            user_email="Please enter a valid email"           
                    
        self.response.write(form.format(username_message= user_message, 
                                  password_message= user_password, 
                                  password_match_message= match_password,
                                  email_message= user_email
                                  ))
            # /welcomesean15
        #else:
        #   self.response.('/')
            
                
        # error = "."
            #self.response.write(error)
            #self.redirect("/?error=" + cgi.escape(error, quote=True))
            #params['error_username'] = "Please enter a valid username."
            #have_error = True
            
        #if (not password) or (password.strip() == ""):
            #error = "Please enter a username."
            #self.response.write(error)
            #self.redirect("/?error=" + cgi.escape(error, quote=True))
            #params['error_password'] = "Please enter a valid password."
            #have_error = True
            
        #if have_error:
        #    self.render('signup-form.html', **params)
        #else:
        #    self.redirect('/unit2/welcome?username=' + username)
        
        #              self.write.form2    
        #message = self.request.get("message") # hello</textarea>hello
        #rotation = int(self.request.get("rotation")) # 0 
        #encrypted_message = caesar.encrypt(message, rotation) # hello</textarea>hello
        #escaped_message = cgi.escape(encrypted_message) # hello&lt;/textarea&gt;hello
        #content = build_page(escaped_message)
        #self.response.write(content)
        
        #originalform = form.format("","","","","","")
        #page footer

#class Welcome(webapp2.RequestHandler):
class Welcome(webapp2.RequestHandler):
       def get(self):
            username = self.request.get('username')
            if valid_username(username):
                 self.response.write(welcome.format(username = username))
            
                
welcome = """
<!DOCTYPE html>
    
<html>
<head>
    <title>
        User Signup
    </title>
</head>

<body>
    <h2>Welcome, {username}!</h2>
</body>
</html>
"""
                
#class TestHandler(webapp2.RequestHandler):
#    """ Handles requests coming in to '/add'
#        e.g. www.user-signup.com/add
#    """
#    def get(self):

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
