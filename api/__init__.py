from flask import Blueprint

blueprint=Blueprint('api',__name__)

from api import api_user,tokens
