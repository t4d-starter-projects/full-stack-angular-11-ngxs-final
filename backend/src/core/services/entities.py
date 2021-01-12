from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from typing import Dict, ClassVar

from src.core.interfaces.logging import LoggingInterface
from src.core.interfaces.data_session import DataSessionInterface


class Entities:

    @staticmethod
    def create_schema(entity_model):
        class EntitySchema(SQLAlchemyAutoSchema):
            class Meta:
                model = entity_model

        return EntitySchema

    def __init__(self, logging: LoggingInterface,
                 data_session: DataSessionInterface,
                 model: ClassVar,
                 model_key_field: str):
        self.logging = logging
        self.Session = data_session.get_session()
        self.Model = model
        self.EntitySchema = self.create_schema(model)
        self.model_key_field = model_key_field

    def all(self) -> Dict:
        session = self.Session()
        entities = session.query(self.Model).all()
        entities_result = self.EntitySchema(many=True).dump(entities)
        session.close()

        return entities_result

    def one_by_id(self, entity_id: int) -> Dict:
        filter_args = {
            self.model_key_field: entity_id
        }

        session = self.Session()
        entity = session.query(self.Model).filter_by(
            **filter_args).one_or_none()
        entity_result = self.EntitySchema().dump(entity)
        session.close()

        return entity_result

    def append_one(self, new_entity: Dict) -> Dict:
        entity = self.Model(**new_entity)

        session = self.Session()
        session.add(entity)
        session.commit()
        entity_result = self.EntitySchema().dump(entity)
        session.close()

        return entity_result

    def replace_one(self, entity: Dict) -> None:
        filter_args = {
            self.model_key_field: entity[self.model_key_field]
        }

        session = self.Session()
        session.query(self.Model).filter_by(
            **filter_args).update(entity)
        session.commit()
        session.close()

        return None

    def remove_one(self, entity_id: int) -> None:
        filter_args = {
            self.model_key_field: entity_id
        }

        session = self.Session()
        session.query(self.Model).filter_by(**filter_args).delete()
        session.commit()
        session.close()

        return None
