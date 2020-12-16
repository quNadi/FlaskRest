import os
class Config(object):
    PUBLIC_KEY=os.environ.get('SECRET_KEY') or 'suicide1'