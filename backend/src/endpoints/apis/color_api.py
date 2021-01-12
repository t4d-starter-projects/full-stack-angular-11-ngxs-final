from flask import Blueprint, jsonify, current_app, request
from dependency_injector.wiring import inject, Provide
import humps

from ..json_schemas.color_schema import ColorSchema
from ..schema_utils import get_new_entity_fields

from src.tasks.tasks_container import Tasks


new_color_fields = get_new_entity_fields(ColorSchema, 'color_id')

color_api = Blueprint('color_api', __name__)


@color_api.route('/colors')
@inject
def get_colors(all_colors_task=Provide[Tasks.all_colors]):
    colors = all_colors_task.run()

    color_schema = ColorSchema(many=True)
    colors_json = color_schema.dump(colors)

    return jsonify(humps.camelize(colors_json))


@color_api.route('/colors/<color_id>')
@inject
def one_color(
        color_id: str,
        one_color_by_id_task=Provide[Tasks.one_color_by_id]):

    color = one_color_by_id_task.run(int(color_id))

    color_schema = ColorSchema()
    color_result = color_schema.dump(color)

    return jsonify(humps.camelize(color_result))


@color_api.route('/colors', methods=['POST'])
@inject
def append_color(append_color_task=Provide[Tasks.append_color]):
    posted_color: ColorSchema = ColorSchema(
        only=new_color_fields
    ).load(humps.decamelize(request.get_json()))

    color = append_color_task.run(posted_color)

    color_result = ColorSchema().dump(color)

    return jsonify(humps.camelize(color_result)), 201


@color_api.route('/colors/<color_id>', methods=['PUT'])
@inject
def replace_color(
        color_id: str,
        replace_color_task=Provide[Tasks.replace_color]):
    color = ColorSchema().load(humps.decamelize(request.get_json()))

    if color['color_id'] != int(color_id):
        return jsonify(''), 400

    replace_color_task.run(color)

    return jsonify(''), 204


@color_api.route('/colors/<color_id>', methods=['DELETE'])
@inject
def remove_color(
        color_id: str,
        remove_color_task=Provide[Tasks.remove_color]):
    remove_color_task.run(int(color_id))

    return jsonify(''), 204
