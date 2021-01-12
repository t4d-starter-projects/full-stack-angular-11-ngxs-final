from marshmallow import Schema, fields


class UserSchema(Schema):
    user_id = fields.Integer()
    user_kind = fields.String()
    username = fields.String()
    display_name = fields.String()
    roles = fields.List(fields.String())
    is_authenticated = fields.Boolean()
    is_active = fields.Boolean()
    is_anonymous = fields.Boolean()
    roles = fields.List(fields.String())
