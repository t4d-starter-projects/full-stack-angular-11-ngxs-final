from marshmallow import Schema, fields


class UserHasOneOrMoreRolesSchema(Schema):
    roles = fields.List(fields.String())
