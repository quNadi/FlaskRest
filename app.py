from flask import Flask
from flask_restful import Api, Resource,reqparse ,fields ,marshal_with,abort
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///noteerrr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)



from api_rest import ApiData

api.add_resource(ApiData, "/api/<int:id>")

if __name__=="__main__":
    app.run(debug=True)