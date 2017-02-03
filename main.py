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

def Build_Page(textarea_content):

    form = """
    <table>
        <tr>
        <td>
        <label>{0}</label>
        </td>
        <td>
        <label>Username: <input type="text" name="username"/></label>
        </td></tr>
    
        <tr>
        <td>
        <label>{1}</label>
        </td>
        <td>
        <label>Password: <input type="text" name="password"/></label>
        </td></tr>
    
        <tr>
        <td> 
        <label>{2}</label>
        </td>
        <td>
        <label>Verify Password: <input type="text" name="verify_password"/></label>
        </td></tr>
    
        <tr>
        <td>
        <label>{3}</label>
        </td>
        <td>
        <label>Email (optional): <input type="text" name="email"/></label>
        </td></tr>
    
    </table>
    """
    submit = "<input type = 'submit'/>"
    form2 = ("<form method='post'>" 
            + form + submit + "</form>").format("Please enter a username", "Please enter a password", "Passwords must match","Please enter a valid email")
            
    header = "<h1>User Signup</h1>" 
    
    return header + form2
        
class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = Build_Page("")
        self.response.write(content)
        
    def post(self):
        # look inside the request to figure out what the user typed
        username = self.request.get("username")
        password = self.request.get("password")
        verify_password = self.request.get("verify_password")
        email = self.request.get("email")
        # if the user typed nothing at all, redirect
        if (not username) or (username.strip() == ""):
            error = "Please enter a username."
            self.response.write(error)
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            
        if (not password) or (username.strip() == ""):
            error = "Please enter a username."
            self.response.write(error)
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            
        """if (not username) or (username.strip() == ""):
            error = "Please enter a username."
            self.response.write(error)
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            
        if (not username) or (username.strip() == ""):
            error = "Please enter a username."
            self.response.write(error)
            self.redirect("/?error=" + cgi.escape(error, quote=True))"""
        
        #              self.write.form2    
        #message = self.request.get("message") # hello</textarea>hello
        #rotation = int(self.request.get("rotation")) # 0 
        #encrypted_message = caesar.encrypt(message, rotation) # hello</textarea>hello
        #escaped_message = cgi.escape(encrypted_message) # hello&lt;/textarea&gt;hello
        #content = build_page(escaped_message)
        #self.response.write(content)
        
        #formoriginalform = form.format("","","","","","")
        #page footer

#class TestHandler(webapp2.RequestHandler):
#    """ Handles requests coming in to '/add'
#        e.g. www.user-signup.com/add
#    """
#    def get(self):

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    #('/', TestHandler)
], debug=True)
