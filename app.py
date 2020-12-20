from flask import Flask,request,jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///noteerrr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
ma=Marshmallow(app)

from models import DataModel,data_schema,data_all_schema


@app.route('/datapi',methods=['POST'])
def add_data():
    name=request.json['name']
    content=request.json['content']
    new_data=DataModel(name,content)
    db.session.add(new_data)
    db.session.commit()
    return data_schema.jsonify(new_data)

@app.route('/datapi',methods=['GET'])
def get_data():
        all_data=DataModel.query.all()
        result=data_all_schema.dump(all_data)
        return jsonify(result)




if __name__=="__main__":
    app.run(debug=True)