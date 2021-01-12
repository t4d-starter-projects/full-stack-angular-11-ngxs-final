from sqlalchemy import Column, String, Integer, Text
from .entity import Base


class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)
    description = Column(Text)

    def __init__(self, category_name, description):
        self.category_name = category_name
        self.description = description
