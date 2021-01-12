from marshmallow import Schema, fields


class EmployeeSchema(Schema):
    employee_id = fields.Integer()
    last_name = fields.Str()
    first_name = fields.Str()
    title = fields.Str()
    title_of_courtesy = fields.Str()
    birth_date = fields.Str()
    hire_date = fields.Str()
    address = fields.Str()
    city = fields.Str()
    region = fields.Str()
    postal_code = fields.Str()
    country = fields.Str()
    home_phone = fields.Str()
    extension = fields.Str()
    notes = fields.Str()
    reports_to = fields.Integer()
    username = fields.Str()
    password = fields.Str()
