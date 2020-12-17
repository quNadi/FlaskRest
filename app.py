from flask import Flask , Blueprint
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy
import config



app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///noteerrr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False



db=SQLAlchemy(app)

from api import blueprint
app.register_blueprint(blueprint,url_prefix='/api')

if __name__=='__main_':
    app.run(debug=True)








