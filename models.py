from app import db
from sqlalchemy import func
from flask import current_app,request,url_for

from datetime import datetime,timedelta
import base64
import os

class UserModel(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    notes=db.Column(db.String(200))
    token=db.Column(db.String(32),index=True,unique=True)
    token_exp=db.Column(db.DateTime)



    def get_token(self,expires_in=3600):
        now=datetime.utcnow()
        if self.token and self.token_exp > now+timedelta(seconds=60):
            return self.token
        self.token=base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_exp=now+timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_exp=datetime.utcnow()-timedelta(seconds=1)



 ##########################################3
    def to_json(self):
        json_user ={
            'id':self.id,
            'username':self.username,
            'notes':self.notes,
            '_links':{
                'self': url_for('api.get_user', id=self.id),
            }
        }
        return json_user

    def from_json(self,data,new_user=False):
        for f in ['username']:
            if f in data:
                setattr(self,f,data[f])
############################



    @staticmethod
    def check_token(token):
        user=UserModel.query.filter_by(token=token).first()
        if user is None or user.token_exp<datetime.utcnow():
            return None
        return user

db.create_all()