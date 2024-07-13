from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Settings(Base):
    __tablename__ = 'settings'
    settingsid = Column(Integer, primary_key=True)
    units = Column(String)
    cal_tol = Column(String)
    proc_tol = Column(String)
    cal_freq = Column(String)
    criticality = Column(String)