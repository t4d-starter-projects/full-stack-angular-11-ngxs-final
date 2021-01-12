from marshmallow import Schema, fields


class CategorySchema(Schema):
    category_id = fields.Int()
    category_name = fields.Str()
    description = fields.Str()
