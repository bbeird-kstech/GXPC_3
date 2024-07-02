from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EquipmentOwner(Base):
    __tablename__ = 'equipment_owner'
    clientid = Column(Integer, primary_key=True)
    client_name = Column(String)
    company_phone = Column(String)
    contact_name = Column(String)
    contact_phone = Column(String)
    contact_email = Column(String)
    archive_flag = Column(Boolean)
