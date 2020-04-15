################################
from NamingApp import db
class N2(db.Model):

    __tablename__ = 'names'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name
