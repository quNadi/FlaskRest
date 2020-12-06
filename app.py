from flask import Flask
from flask_restful import Api,Resource
from backend.db import db

def create_app():
    application=Flask(__name__)
    api=Api()

    db.init_app(application)
    application.db=db



    return application



if __name__=="__main__":
    app=create_app()
    app.app_context().push()
    app.db.create_all()

