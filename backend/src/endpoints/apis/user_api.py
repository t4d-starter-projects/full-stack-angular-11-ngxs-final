from flask import Blueprint, request, jsonify
from dependency_injector.wiring import inject, Provide
import humps

from ..json_schemas.user_schema import UserSchema
from ..json_schemas.login_user_schema import LoginUserSchema
from ..json_schemas.user_change_password_schema import UserChangePasswordSchema
from ..json_schemas.user_has_one_or_more_roles_schema import \
    UserHasOneOrMoreRolesSchema
from ..security_utils import create_token, check_for_refresh_token, authorize, www_auth_header

from src.tasks.tasks_container import Tasks

user_api = Blueprint('user_api', __name__)


@user_api.route('/users/login', methods=['POST'])
@inject
def login(login_task=Provide[Tasks.login_user]):
    login_user = LoginUserSchema(only=('username', 'password', 'kind')).load(
        humps.decamelize(request.get_json()))

    user = login_task.run(login_user)

    if user is None:
        return 'User not found', 404

    user_schema = UserSchema(many=False)
    user_result = user_schema.dump(user)

    user_result['access_token'] = create_token(user_result)

    user_result['refresh_token'] = create_token(user_result,
                                                False,
                                                60)

    return jsonify(humps.camelize(user_result))


@user_api.route('/users/refresh', methods=['GET'])
@check_for_refresh_token
@inject
def refresh(refresh_user_task=Provide[Tasks.refresh_user]):
    if not refresh_user_task.run(request.token_data):
        return 'Invalid authorization token', 401, www_auth_header

    refreshed_user = {
        'access_token': create_token(request.token_data),
        'refresh_token': create_token(request.token_data, False, 60)
    }

    return jsonify(humps.camelize(refreshed_user))


@user_api.route('/users/change-password', methods=['POST'])
@authorize(['user'])
@inject
def change_password(
        user_change_password_task=Provide[Tasks.user_change_password]):
    user_change_password = UserChangePasswordSchema(
        only=('username', 'user_kind', 'old_password', 'new_password')
    ).load(humps.decamelize(request.get_json()))

    if not user_change_password_task.run(user_change_password):
        return 'Password not changed', 400

    return '', 200


@user_api.route('/users/has_one_or_more_roles', methods=['POST'])
@authorize(['user'])
@inject
def has_one_or_more_roles(
        user_has_one_or_more_roles_task=Provide[
            Tasks.user_has_one_or_more_roles]
):
    user_has_one_or_more_roles = UserHasOneOrMoreRolesSchema(
        only=(['roles'])
    ).load(humps.decamelize(request.get_json()))

    return jsonify(humps.camelize({
        'has_role': user_has_one_or_more_roles_task.run(
            request.token_data['username'], user_has_one_or_more_roles[
                                                   'roles'])})), 200
