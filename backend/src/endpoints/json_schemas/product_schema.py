from marshmallow import Schema, fields


class ProductSchema(Schema):
    product_id = fields.Integer()
    product_name = fields.String()
    supplier_id = fields.Integer()
    category_id = fields.Integer()
    quantity_per_unit = fields.String()
    unit_price = fields.Number()
    units_in_stock = fields.Integer()
    units_on_order = fields.Integer()
    reorder_level = fields.Integer()
    discontinued = fields.Integer()
