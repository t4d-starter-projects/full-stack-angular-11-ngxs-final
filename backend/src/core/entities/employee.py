from sqlalchemy import Column, SmallInteger, String, Date, Text

from .entity import Base


class Employee(Base):
    __tablename__ = 'employees'
    employee_id = Column(SmallInteger, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    title = Column(String)
    title_of_courtesy = Column(String)
    birth_date = Column(Date)
    hire_date = Column(Date)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    home_phone = Column(String)
    extension = Column(String)
    notes = Column(Text)
    reports_to = Column(SmallInteger)
    username = Column(String)
    password = Column(String)

    def __init__(self, employee_id, last_name, first_name, title,
                 title_of_courtesy, birth_date, hire_date, address, city,
                 region, postal_code, country, home_phone, extension, photo,
                 notes, reports_to, photo_path, username, password):
        self.employee_id = employee_id
        self.last_name = last_name
        self.first_name = first_name
        self.title = title
        self.title_of_courtesy = title_of_courtesy
        self.birth_date = birth_date
        self.hire_date = hire_date
        self.address = address
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.country = country
        self.home_phone = home_phone
        self.extension = extension
        self.photo = photo
        self.notes = notes
        self.reports_to = reports_to
        self.photo_path = photo_path
        self.username = username
        self.password = password

    def display_name(self):
        return self.first_name + ' ' + self.last_name
