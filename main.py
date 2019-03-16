import webapp2
from model import Account, Branch
from google.appengine.ext import ndb

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
        self.response.write(open('header.html').read())
        an = self.request.get('tfAcNo')
        ahn = self.request.get('tfAcHName')
        amn = self.request.get('tfHMNo')
        ab = self.request.get('tfAcBalance')
        city = self.request.get('ddCity')
        # getting branch
        bc = self.request.get('tfBC')
        bn = self.request.get('tfBN')
        bm = self.request.get('tfBM')
        bp = self.request.get('tfBP')

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
        # creating an instance of Branch
        br = Branch()
        br.BCode = int(bc)
        br.BName = bn
        br.BManager = bm
        br.BPINCode = int(bp)
        # setting to account instance
        act.BranchInfo = br
        # storing into database
        key = act.put()
        self.response.write(key.urlsafe())

class SearchAccount(webapp2.RequestHandler):
    def get(self):
        self.response.write(open('header.html').read())
        an = self.request.get("tfAcNo")
        # query from Googe NDB
        result = Account.query(ndb.OR(Account.AcNo == int(an), Account.AcBalance >= 40000))
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

class DeleteAccount(webapp2.RequestHandler):
    'to delete an account'
    def get(self):
        urlsafe = self.request.get('urlsafe')
        result = Account.query()
        for item in result:
            if item.key.urlsafe() == urlsafe:
                self.response.write(str( item.key.id() ) +"<br/>")
                self.response.write(str( item.key.kind() )+"<br/>" )
                self.response.write(str( item.key.urlsafe() )+"<br/>" )
                self.response.write(str( item.key.delete() )+"<br/>" )

start = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/appform', AppForm),
    ('/htmladdaccount', HTMLAddAccount),
    ('/htmlsearchaccount', HTMLSearchAccount),
    ('/searchaccount', SearchAccount),
    ('/addaccount', AddAccount),
    ('/deleteaccount', DeleteAccount)
], debug = True)