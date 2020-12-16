from flask import g

@api.route('/tokens/',methods=['POST'])
def get_token():
    if g.current