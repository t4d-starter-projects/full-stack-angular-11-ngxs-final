from flask import Blueprint, jsonify, current_app, request
from dependency_injector.wiring import inject, Provide
import humps

from ..json_schemas.supplier_schema import SupplierSchema
from ..schema_utils import get_new_entity_fields
from ..security_utils import authorize

from src.tasks.tasks_container import Tasks

new_supplier_fields = get_new_entity_fields(SupplierSchema, 'supplier_id')

supplier_api = Blueprint('supplier_api', __name__)


@supplier_api.route('/suppliers')
@authorize(roles=['user'])
@inject
def get_suppliers(all_suppliers_task=Provide[Tasks.all_suppliers]):

    suppliers = all_suppliers_task.run()

    # serialize to JSON encoded string
    supplier_schema = SupplierSchema(many=True)
    suppliers_json = supplier_schema.dump(suppliers)

    # return a JSON response
    return jsonify(humps.camelize(suppliers_json))


@supplier_api.route('/categories/<supplier_id>')
@authorize(roles=['user'])
@inject
def one_supplier(
        supplier_id: str,
        one_supplier_by_id_task=Provide[Tasks.one_supplier_by_id]):
    supplier = one_supplier_by_id_task.run(int(supplier_id))

    supplier_schema = SupplierSchema()
    supplier_result = supplier_schema.dump(supplier)

    return jsonify(humps.camelize(supplier_result))


@supplier_api.route('/categories', methods=['POST'])
@authorize(roles=['user'])
@inject
def append_supplier(append_supplier_task=Provide[Tasks.append_supplier]):
    posted_supplier: SupplierSchema = SupplierSchema(
        only=new_supplier_fields
    ).load(humps.decamelize(request.get_json()))

    supplier = append_supplier_task.run(posted_supplier)

    supplier_result = SupplierSchema().dump(supplier)

    return jsonify(humps.camelize(supplier_result)), 201


@supplier_api.route('/categories/<supplier_id>', methods=['PUT'])
@authorize(roles=['user'])
@inject
def replace_supplier(
        supplier_id: str,
        replace_supplier_task=Provide[Tasks.replace_supplier]):
    supplier = SupplierSchema().load(humps.decamelize(request.get_json()))

    if supplier['supplier_id'] != int(supplier_id):
        return jsonify(''), 400

    replace_supplier_task.run(supplier)

    return jsonify(''), 204


@supplier_api.route('/categories/<supplier_id>', methods=['DELETE'])
@authorize(roles=['user'])
@inject
def remove_supplier(
        supplier_id: str,
        remove_supplier_task=Provide[Tasks.remove_supplier]):
    remove_supplier_task.run(int(supplier_id))

    return jsonify(''), 204
