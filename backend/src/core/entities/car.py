from sqlalchemy import Column, String, Integer, Float, SmallInteger
from .entity import Base


class Car(Base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(SmallInteger)
    color = Column(String)
    price = Column(Float)

    def __init__(self, make, model, year, color, price):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
