def get_new_entity_fields(schema, key_field):
    return tuple(filter(lambda key: key != key_field,
                        schema().fields.keys()))
