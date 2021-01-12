from sqlalchemy import Column, String, Integer
from .entity import Base


class Color(Base):
    __tablename__ = 'colors'

    color_id = Column(Integer, primary_key=True)
    color_name = Column(String)
    hexcode = Column(String)

    def __init__(self, color_name, hexcode):
        self.color_name = color_name
        self.hexcode = hexcode
