from app import db
from flask_restful import fields

class DataModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    content=db.Column(db.String(300))

    def __repr__(self):
        return f"Data(name={self.name}, content={self.content})"


db.create_all()



resource_fields={
    'id':fields.Integer,
    'name':fields.String,
    'content':fields.String

}