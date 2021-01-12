from flask import Blueprint, jsonify, current_app, request
from dependency_injector.wiring import inject, Provide
import humps

from ..json_schemas.car_schema import CarSchema
from ..schema_utils import get_new_entity_fields

from src.tasks.tasks_container import Tasks


new_car_fields = get_new_entity_fields(CarSchema, 'car_id')

car_api = Blueprint('car_api', __name__)


@car_api.route('/cars')
@inject
def get_cars(all_cars_task=Provide[Tasks.all_cars]):
    cars = all_cars_task.run()

    car_schema = CarSchema(many=True)
    cars_json = car_schema.dump(cars)

    return jsonify(humps.camelize(cars_json))


@car_api.route('/cars/<car_id>')
@inject
def one_car(
        car_id: str,
        one_car_by_id_task=Provide[Tasks.one_car_by_id]):

    car = one_car_by_id_task.run(int(car_id))

    car_schema = CarSchema()
    car_result = car_schema.dump(car)

    return jsonify(humps.camelize(car_result))


@car_api.route('/cars', methods=['POST'])
@inject
def append_car(append_car_task=Provide[Tasks.append_car]):
    posted_car: CarSchema = CarSchema(
        only=new_car_fields
    ).load(humps.decamelize(request.get_json()))

    car = append_car_task.run(posted_car)

    car_result = CarSchema().dump(car)

    return jsonify(humps.camelize(car_result)), 201


@car_api.route('/cars/<car_id>', methods=['PUT'])
@inject
def replace_car(
        car_id: str,
        replace_car_task=Provide[Tasks.replace_car]):
    car = CarSchema().load(humps.decamelize(request.get_json()))

    if car['car_id'] != int(car_id):
        return jsonify(''), 400

    replace_car_task.run(car)

    return jsonify(''), 204


@car_api.route('/cars/<car_id>', methods=['DELETE'])
@inject
def remove_car(
        car_id: str,
        remove_car_task=Provide[Tasks.remove_car]):
    remove_car_task.run(int(car_id))

    return jsonify(''), 204
