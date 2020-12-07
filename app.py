from flask import Flask
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///noteerrr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
cors=CORS(app)
app.config['CORS_HEADERS']= 'Content-Type'

db=SQLAlchemy(app)
api=Api(app)

from backend.rest_api import NotesList,NoteRecord

api.add_resource(NotesList,'/')
api.add_resource(NoteRecord, '/note/<note_id>')

if __name__=='__main_':
    app.run(debug=True)








