from flask import Blueprint, jsonify, current_app, request
from dependency_injector.wiring import inject, Provide
import humps

from ..json_schemas.product_schema import ProductSchema
from ..schema_utils import get_new_entity_fields
from ..security_utils import authorize

from src.tasks.tasks_container import Tasks


new_product_fields = get_new_entity_fields(ProductSchema, 'product_id')

product_api = Blueprint('product_api', __name__)


@product_api.route('/products')
@authorize(roles=['user'])
@inject
def get_products(all_products_task=Provide[Tasks.all_products]):
    products = all_products_task.run()

    product_schema = ProductSchema(many=True)
    products_json = product_schema.dump(products)

    return jsonify(humps.camelize(products_json))


@product_api.route('/categories/<product_id>')
@authorize(roles=['user'])
@inject
def one_product(
        product_id: str,
        one_product_by_id_task=Provide[Tasks.one_product_by_id]):

    product = one_product_by_id_task.run(int(product_id))

    product_schema = ProductSchema()
    product_result = product_schema.dump(product)

    return jsonify(humps.camelize(product_result))


@product_api.route('/categories', methods=['POST'])
@authorize(roles=['user'])
@inject
def append_product(append_product_task=Provide[Tasks.append_product]):
    posted_product: ProductSchema = ProductSchema(
        only=new_product_fields
    ).load(humps.decamelize(request.get_json()))

    product = append_product_task.run(posted_product)

    product_result = ProductSchema().dump(product)

    return jsonify(humps.camelize(product_result)), 201


@product_api.route('/categories/<product_id>', methods=['PUT'])
@authorize(roles=['user'])
@inject
def replace_product(
        product_id: str,
        replace_product_task=Provide[Tasks.replace_product]):
    product = ProductSchema().load(humps.decamelize(request.get_json()))

    if product['product_id'] != int(product_id):
        return jsonify(''), 400

    replace_product_task.run(product)

    return jsonify(''), 204


@product_api.route('/categories/<product_id>', methods=['DELETE'])
@authorize(roles=['user'])
@inject
def remove_product(
        product_id: str,
        remove_product_task=Provide[Tasks.remove_product]):
    remove_product_task.run(int(product_id))

    return jsonify(''), 204
