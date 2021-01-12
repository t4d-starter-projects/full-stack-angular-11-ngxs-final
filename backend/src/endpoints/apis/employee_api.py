from flask import Blueprint, jsonify, current_app, request
from dependency_injector.wiring import inject, Provide
import humps

from ..json_schemas.employee_schema import EmployeeSchema
from ..schema_utils import get_new_entity_fields
from ..security_utils import authorize

from src.tasks.tasks_container import Tasks

new_employee_fields = get_new_entity_fields(EmployeeSchema, 'employee_id')

employee_api = Blueprint('employee_api', __name__)


@employee_api.route('/employees')
@authorize(roles=['admin'])
@inject
def all_employees(all_employees_task=Provide[Tasks.all_employees]):

    employees = all_employees_task.run()

    employee_schema = EmployeeSchema(many=True)
    employees_result = employee_schema.dump(employees)

    return jsonify(humps.camelize(employees_result))


@employee_api.route('/employees/<employee_id>')
@authorize(roles=['admin'])
@inject
def one_employee(
        employee_id: str,
        one_employee_by_id_task=Provide[Tasks.one_employee_by_id]):

    employee = one_employee_by_id_task.run(int(employee_id))

    employee_schema = EmployeeSchema()
    employee_result = employee_schema.dump(employee)

    return jsonify(humps.camelize(employee_result))


@employee_api.route('/employees', methods=['POST'])
@authorize(roles=['admin'])
@inject
def append_employee(append_employee_task=Provide[Tasks.append_employee]):
    posted_employee: EmployeeSchema = EmployeeSchema(
        only=new_employee_fields
    ).load(humps.decamelize(request.get_json()))

    employee = append_employee_task.run(posted_employee)

    employee_result = EmployeeSchema().dump(employee)

    return jsonify(humps.camelize(employee_result)), 201


@employee_api.route('/employees/<employee_id>', methods=['PUT'])
@authorize(roles=['admin'])
@inject
def replace_employee(
        employee_id: str,
        replace_employee_task=Provide[Tasks.replace_employee]):
    employee = EmployeeSchema().load(humps.decamelize(request.get_json()))

    if employee['employee_id'] != int(employee_id):
        return jsonify(''), 400

    replace_employee_task.run(employee)

    return jsonify(''), 204


@employee_api.route('/employees/<employee_id>', methods=['DELETE'])
@authorize(roles=['admin'])
@inject
def remove_employee(
        employee_id: str,
        remove_employee_task=Provide[Tasks.remove_employee]):
    remove_employee_task.run(int(employee_id))

    return jsonify(''), 204
