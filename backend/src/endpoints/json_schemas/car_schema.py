from marshmallow import Schema, fields


class CarSchema(Schema):
    car_id = fields.Integer()
    make = fields.String()
    model = fields.String()
    year = fields.Integer()
    color = fields.String()
    price = fields.Number()
