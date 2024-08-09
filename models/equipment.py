from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from .base import Base


class Equipment(Base):
    __tablename__ = 'equipment'
    equipment_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('equipment_owner.clientid'), nullable=False)
    client_equip_num = Column(String)
    description = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    serial_number = Column(String)
    cal_frequency = Column(String)
    criticality = Column(String)
    num_cal_params = Column(Integer)


class CalParameters(Base):
    __tablename__ = 'cal_parameters'
    parameter_id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_id = Column(Integer, ForeignKey('equipment.equipment_id'), nullable=False)
    parameter_name = Column(String)
    units = Column(String)
    min_range = Column(Numeric(6, 3))
    max_range = Column(Numeric(6, 3))
    procedure_number = Column(String)
    num_cal_pts = Column(Integer)


class CalNomPt(Base):
    __tablename__ = 'cal_nom_pt'
    point_id = Column(Integer, primary_key=True, autoincrement=True)
    cal_param_id = Column(Integer, ForeignKey('cal_parameters.parameter_id'), nullable=False)
    nom_value = Column(Integer)
    cal_tol = Column(Numeric(6, 3))
    proc_tol = Column(Numeric(6, 3))
