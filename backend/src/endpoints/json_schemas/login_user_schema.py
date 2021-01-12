from marshmallow import Schema, fields


class LoginUserSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    kind = fields.Str()
