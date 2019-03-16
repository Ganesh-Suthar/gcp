from google.appengine.ext import ndb

class Branch(ndb.Model):
    'to describe a Model'
    BCode = ndb.IntegerProperty(required=True)
    BName = ndb.StringProperty(default="Regional Office")
    BManager = ndb.StringProperty()
    BPINCode = ndb.IntegerProperty()

class Account(ndb.Model):
    '''to describe an account detail'''
    AcNo = ndb.IntegerProperty(required=True)
    AcHName = ndb.StringProperty()
    AcMobNo = ndb.StringProperty()
    AcBalance = ndb.FloatProperty()
    City = ndb.StringProperty()
    BranchInfo = ndb.StructuredProperty(Branch)
    Rewards = ndb.ComputedProperty(lambda self:self.AcBalance*0.1)

