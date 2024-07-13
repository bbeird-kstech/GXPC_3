from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey
from .base import Base

class Equipment(Base):
    __tablename__ = 'equipment'
    equipment_id = Column(Integer, primary_key=True, autoincrement=True)
    client_inst_id = Column(String)
    description = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    serial_number = Column(String)
    num_cal_pts = Column(Integer)
    units = Column(String)
    cal_tol = Column(Numeric(6, 3))
    proc_tol = Column(Numeric(6, 3))
    frequency = Column(String)
    criticality = Column(String)
    client = Column(Integer, ForeignKey('equipment_owner.clientid'), nullable=False)
