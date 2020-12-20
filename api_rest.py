from flask_restful import Resource,abort,marshal_with ,reqparse
from models import DataModel,resource_fields
from app import db


data_args=reqparse.RequestParser()
data_args.add_argument("name",type=str,help="name is necessary ")
data_args.add_argument("content",type=str,help="name is necessary ")

class ApiData(Resource):
    @marshal_with(resource_fields)
    def get(self,id_data):
        result=DataModel.query.filtr_by(id=id_data).first()
        if not result:
            abort(404,message="we cant find")
        return result

    @marshal_with(resource_fields)
    def put(self,id_data):
        args=data_args.parse_args()
        result=DataModel.query.filtr_by(id=id_data).first()
        if result:
            abort(409,message="we have this id")
        data=DataModel(id=id_data,name=args['name'],content=args['content'])
        db.session.add(data)
        db.session.commit()
        return data,201

    @marshal_with(resource_fields)
    def patch(self, id_data):
        args = data_args.parse_args()
        result = DataModel.query.filtr_by(id=id_data).first()
        if not result:
            abort(404,message="can't find so i can't update")
        if "name" in args:
            result.name=args['name']
        if "content" in args:
            result.content=args['content']

        db.session.add(result)
        db.session.commit()
        return result

    def delete(self,id_data):
        args = data_args.parse_args()
        result = DataModel.query.filtr_by(id=id_data).first()
