from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from ..models import User
from . import api
from .errors import unauthorized, forbidden

auth = HTTPBasicAuth()


@auth.verify_password
def verify_token(token):
    if token == '':
        return False
    else:
        g.current_user = User.verify_auth_token(token)
        g.token_used = True
        return g.current_user is not None


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@api.route('/tokens/', methods=['POST'])
def get_token():
    if g.current_user.is_anonymous or g.token_used:
        return unauthorized('Invalid credentials')
    return jsonify({'token': g.current_user.generate_auth_token(
        expiration=3600), 'expiration': 3600})