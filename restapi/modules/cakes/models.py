__author__ = 'haukurk'

from restapi.modules.base import BaseModel, db
from marshmallow import Serializer, fields
from sqlalchemy import Column,String,Float,Integer,DateTime,Date,Time
from DateTime import DateTime


class Cake(BaseModel):
    """
    Cake class that defines how cake object are kept in the database.
    """
    __tablename__='exampletest'
    ex1 = db.Column(db.String(40), unique=False)
    ex2 = db.Column(db.String(40), unique=False)
    ex3 = db.Column(db.String(50), unique=False)
    ex4 = db.Column(db.Date)
    ex5 = db.Column(db.Time) 

    def __init__(self,ex1,ex2,ex3,ex4,ex5):
        self.ex1 = ex1
        self.ex2 = ex2
        self.ex3 = ex3
        self.ex4 = ex4
        self.ex5 = ex5

    def as_dict(self):
        Cake_dict = {}
        for C in self.__table__.columns:
            Cake_dict[C.ex3] = getattr(self, C.ex3)
        return Cake_dict  
         
    def __repr__(self):
        return "<Cake %s>" % self.ex3


class CakeSerializer(Serializer):
    """
    Serializer for the SQLALchemy class. The magic is performed with marshmallow module.
    """

    class Meta:
        fields = (ex1,ex2,ex3,ex4,ex5)
