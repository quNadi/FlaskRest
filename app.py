from flask import Flask , Blueprint
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy
import config



app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///noteerrr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False



db=SQLAlchemy(app)

api=Blueprint('api',__name__)
app.register_blueprint(api,url_prefix='/api/v1')

if __name__=='__main_':
    app.run(debug=True)








