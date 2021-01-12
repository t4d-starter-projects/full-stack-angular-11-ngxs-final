from flask import request, current_app, jsonify
from functools import wraps
import jwt
import datetime

authorization_header_prefix = 'Bearer '
authorization_header_prefix_len = len(authorization_header_prefix)
www_auth_header = {
    'WWW-Authenticate': 'Token realm="Backend", charset="UTF-8"'}


def get_token_data(token):
    return jwt.decode(token, current_app.config['SECRET_KEY'])


def authorize(roles=[]):
    def check_for_access_token(func):
        @wraps(func)
        def wrapped(*args, **kwargs) -> object:
            authorization_header = request.headers.get('Authorization')
            if not authorization_header:
                return 'Missing authorization header', 400

            token = authorization_header[authorization_header_prefix_len:]
            if not token:
                return 'Malformed authorization header', 400
            try:
                token_data = get_token_data(token)

                if not token_data['is_access']:
                    return 'Incorrect authorization token sent', 400

                token_roles = set(token_data['roles'])
                authorize_roles = set(roles)
                if len(token_roles.intersection(authorize_roles)) == 0:
                    return 'Not authorized', 403

                request.token_data = token_data
            except:
                return 'Invalid authorization token', 401, www_auth_header

            return func(*args, **kwargs)
        return wrapped
    return check_for_access_token


def check_for_refresh_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs) -> object:
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return 'Missing authorization header', 400

        token = authorization_header[authorization_header_prefix_len:]
        if not token:
            return 'Malformed authorization header', 400
        try:
            token_data = get_token_data(token)
            if not token_data['is_refresh']:
                return 'Incorrect authorization token sent', 400
            request.token_data = token_data
        except:
            return 'Invalid authorization token', 401, www_auth_header

        return func(*args, **kwargs)

    return wrapped


def create_token(user, is_access=True, ttl_minutes=2):
    token = jwt.encode({
        'username': user['username'],
        'display_name': user['display_name'],
        'user_kind': user['user_kind'],
        'roles': user['roles'],
        'is_access': is_access,
        'is_refresh': not is_access,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(
            minutes=ttl_minutes)
    }, current_app.config['SECRET_KEY'])
    return token.decode('utf-8')
