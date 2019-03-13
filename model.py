from google.appengine.ext import ndb

class Account(ndb.Model):
    '''to describe an account detail'''
    AcNo = ndb.IntegerProperty(required=True)
    AcHName = ndb.StringProperty()
    AcMobNo = ndb.StringProperty()
    AcBalance = ndb.FloatProperty()
    City = ndb.StringProperty()

