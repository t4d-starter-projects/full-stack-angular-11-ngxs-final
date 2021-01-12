from flask import Blueprint, jsonify, current_app, request
from dependency_injector.wiring import inject, Provide
import humps

from ..json_schemas.category_schema import CategorySchema
from ..schema_utils import get_new_entity_fields
from ..security_utils import authorize

from src.tasks.tasks_container import Tasks

new_category_fields = get_new_entity_fields(CategorySchema, 'category_id')

category_api = Blueprint('category_api', __name__)


@category_api.route('/categories')
@authorize(roles=['user'])
@inject
def all_categories(all_categories_task=Provide[Tasks.all_categories]):
    categories = all_categories_task.run()

    category_schema = CategorySchema(many=True)
    categories_result = category_schema.dump(categories)

    return jsonify(humps.camelize(categories_result))


@category_api.route('/categories/<category_id>')
@authorize(roles=['user'])
@inject
def one_category(
        category_id: str,
        one_category_by_id_task=Provide[Tasks.one_category_by_id]
):
    category = one_category_by_id_task.run(int(category_id))

    category_schema = CategorySchema()
    category_result = category_schema.dump(category)

    return jsonify(humps.camelize(category_result))


@category_api.route('/categories', methods=['POST'])
@authorize(roles=['user'])
@inject
def append_category(append_category_task=Provide[Tasks.append_category]):
    posted_category: CategorySchema = CategorySchema(
        only=new_category_fields
    ).load(humps.decamelize(request.get_json()))

    category = append_category_task.run(posted_category)

    category_result = CategorySchema().dump(category)

    return jsonify(humps.camelize(category_result)), 201


@category_api.route('/categories/<category_id>', methods=['PUT'])
@authorize(roles=['user'])
@inject
def replace_category(
        category_id: str,
        replace_category_task=Provide[Tasks.replace_category]):
    category = CategorySchema().load(humps.decamelize(request.get_json()))

    if category['category_id'] != int(category_id):
        return jsonify(''), 400

    replace_category_task.run(category)

    return jsonify(''), 204


@category_api.route('/categories/<category_id>', methods=['DELETE'])
@authorize(roles=['user'])
@inject
def remove_category(
        category_id: str,
        remove_category_task = Provide[Tasks.remove_category]):

    remove_category_task.run(int(category_id))

    return jsonify(''), 204
