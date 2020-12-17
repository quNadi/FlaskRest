from api import blueprint
from flask import jsonify,url_for,request
from models import UserModel
from app import db

from api.tokens import token_auth

@blueprint.route('/users<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    return jsonify(UserModel.query.get_or_404(id).to_json())

@blueprint.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    data=UserModel.query.all()
    return jsonify(data)


@blueprint.route('/users', methods=['POST'])
@token_auth.login_required
def create_user():
    data=request.get_json() or {}
    if 'username' not in data:
        return 'must include username'
    if UserModel.query.filter_by(username=data['username']).first():
        return 'please different name'
    user=UserModel()
    user.from_json(data,new_user=True)
    db.session.add(user)
    db.session.commit()
    response=jsonify(user.to_json())
    response.status_code=201
    response.headers['Location']=url_for('api.get_user',id=user.id)
    return response

@blueprint.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    user=UserModel.query.get_or_404(id)
    data=request.get_json() or {}
    if 'username' in data and data['username']!=user.username and UserModel.query.filter_by(username=data['username']).first():
        return 'use diffrent name'

    user.from_json(data,new_user=False)
    db.session.commit()
    return jsonify(user.to_json())