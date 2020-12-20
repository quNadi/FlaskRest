from app import db,ma



class DataModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    content=db.Column(db.Integer)

    def __init__(self,name,content):
        self.name=name
        self.content=content

class DataSchema(ma.Schema):
    class Meta:
        fields=('id','name','content')

data_schema=DataSchema()
data_all_schema=DataSchema(many=True)

db.create_all()



