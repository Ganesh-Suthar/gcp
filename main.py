import webapp2
from model import Account

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(open("header.html").read())
        self.response.write(open("addact.html").read())

class HTMLAddAccount(webapp2.RequestHandler):
    def get(self):
        self.response.write(open("header.html").read())
        self.response.write(open("addact.html").read())

class HTMLSearchAccount(webapp2.RequestHandler):
    def get(self):
        self.response.write(open("header.html").read())
        self.response.write(open("searchaccount.html").read())

class AppForm(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("tfName")
        mno = self.request.get("tfMNo")
        dob = self.request.get("dtDOB")
        self.response.write("<h2>Hello "+name+"</h2>")
        self.response.write("<h2>Mobile No : "+mno+"</h2>")
        self.response.write("<h2>Date of Birth is : "+dob+"</h2>")

class AddAccount(webapp2.RequestHandler):
    def get(self):
        an = self.request.get('tfAcNo')
        ahn = self.request.get('tfAcHName')
        amn = self.request.get('tfHMNo')
        ab = self.request.get('tfAcBalance')
        city = self.request.get('ddCity')
        self.response.write(an+"<br/>")
        self.response.write(ahn+"<br/>")
        self.response.write(amn+"<br/>")
        self.response.write(ab+"<br/>")
        self.response.write(city+"<br/>")
        # creating a model Account
        act = Account()
        act.AcNo = int(an)
        act.AcHName = ahn
        act.AcMobNo = amn
        act.AcBalance = float(ab)
        act.City = city
        # storing into database
        key = act.put()
        self.response.write(key.urlsafe())

class SearchAccount(webapp2.RequestHandler):
    def get(self):
        self.response.write(open('header.html').read())
        an = self.request.get("tfAcNo")
        # query from Googe NDB
        result = Account.query(Account.AcNo == int(an))
        if result:
            self.response.write("<table border='1'>")
            for act in result:
                self.response.write("<tr>")
                self.response.write("<td>"+str(act.AcNo)+"</td>")
                self.response.write("<td>"+act.AcHName+"</td>")
                self.response.write("<td>"+str(act.AcBalance)+"</td>")
                self.response.write("<td>"+str(act.AcMobNo)+"</td>")
                self.response.write("<td>"+act.City+"</td>")
                self.response.write("</tr>")
            self.response.write("</table>")
        else:
            self.response.write("No Data Found")

start = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/appform', AppForm),
    ('/htmladdaccount', HTMLAddAccount),
    ('/htmlsearchaccount', HTMLSearchAccount),
    ('/searchaccount', SearchAccount),
    ('/addaccount', AddAccount)
], debug = True)