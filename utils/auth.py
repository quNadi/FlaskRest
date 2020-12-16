import jwt
from parse import parse
from datetime import datetime, timedelta

import logging

logger=logging.getLogger(__name__)

def encode_token(payload,private_key):
    return jwt.encode(payload,private_key,algorithm='RS256')

def decode_token(token, public_key):
    return jwt.decode(token,public_key,algorithms='RS256')

def generate_token(name,private_key):

    payload={
        'name':name,
        'iat':datetime.utcnow(),
        'exp':datetime.utcnow()+timedelta(days=1)
    }
    token=encode_token(payload,private_key)
    token=token.decode('utf8')
    return f'Bearer {token}'

def validate_token(header,public_key):
    if not header:
        logger.info('no header')
        return None

    parse_result=parse('Bearer {}', header)
    if not parse_result:
        logger.info('wrong format for header')
        return None
    token=parse_result[0]
    try:
        decoded_token=decode_token(token.encode('utf8'),public_key)
    except jwt.exceptions.DecodeError:
        logger.warning("wrong key")
        return None

    except jwt.exceptions.ExpiredSignatureError:
        logger.error('header expired')
        return None
    if 'name' not in decoded_token:
        logger.warning('not have name')
        return None

    logger.info("SUCCESS")
    return decoded_token['name']

