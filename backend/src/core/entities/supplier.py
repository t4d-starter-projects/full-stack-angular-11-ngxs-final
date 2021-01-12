from sqlalchemy import Column, Integer, String, Text
from .entity import Base


class Supplier(Base):
    __tablename__ = 'suppliers'

    supplier_id = Column(Integer, primary_key=True)
    company_name = Column(String)
    contact_name = Column(String)
    contact_title = Column(String)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone = Column(String)
    fax = Column(String)
    homepage = Column(Text)

    def __init__(self, supplier_id, company_name, contact_name, contact_title,
                 address, city, region, postal_code, country, phone, fax,
                 homepage):
        self.supplier_id = supplier_id
        self.company_name = company_name
        self.contact_name = contact_name
        self.contact_title = contact_title
        self.address = address
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.fax = fax
        self.homepage = homepage
