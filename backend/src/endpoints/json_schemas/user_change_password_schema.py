from marshmallow import Schema, fields


class UserChangePasswordSchema(Schema):
    username = fields.String()
    user_kind = fields.String()
    old_password = fields.String()
    new_password = fields.String()
