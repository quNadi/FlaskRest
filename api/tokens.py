from flask_httpauth import HTTPBasicAuth,HTTPTokenAuth
from models import UserModel
from flask import jsonify
from app import db
from api import blueprint

basichttp=HTTPBasicAuth()

token_auth=HTTPTokenAuth()

blueprint.route('/tokens',methods=['POST'])
@basichttp.login_required
def get_token():
    token=basichttp.current_user().get_token()
    db.session.commit()
    return jsonify({'token':token})

@token_auth.verify_token
def verify_token(token):
    return UserModel.check_token(token) if token else None

@token_auth.error_handler
def token_error(status):
    return jsonify({'status':status})