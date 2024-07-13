from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.equipment_owner import EquipmentOwner
from models.settings import Settings
from models.equipment import Equipment
# from models.unit import Unit
# from models.calibration_tolerance import CalibrationTolerance
# from models.process_tolerance import ProcessTolerance
# from models.frequency import Frequency
# from models.criticality import Criticality
# from models.client import Client

DATABASE_URL = 'postgresql://postgres:Kstech070@localhost/GXPC_Dev'


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get_client_names(self):
        session = self.get_session()
        clients = session.query(EquipmentOwner.client_name).all()
        session.close()
        return [client.client_name for client in clients]

    def get_units(self):
        session = self.get_session()
        units = session.query(Settings.units).all()
        session.close()
        return [result.units for result in units if result.units is not None]

    def get_caltol(self):
        session = self.get_session()
        cal_tol = session.query(Settings.cal_tol).all()
        session.close()
        return [result.cal_tol for result in cal_tol if result.cal_tol is not None]

    def get_proctol(self):
        session = self.get_session()
        proc_tol = session.query(Settings.proc_tol).all()
        session.close()
        return [result.proc_tol for result in proc_tol if result.proc_tol is not None]

    def get_calfreq(self):
        session = self.get_session()
        cal_freq = session.query(Settings.cal_freq).all()
        session.close()
        return [result.cal_freq for result in cal_freq if result.cal_freq is not None]

    def get_criticality(self):
        session = self.get_session()
        criticality = session.query(Settings.criticality).all()
        session.close()
        return [result.criticality for result in criticality if result.criticality is not None]

    def get_client_id_by_name(self, client_name):
        session = self.get_session()
        client = session.query(EquipmentOwner).filter_by(client_name=client_name).first()
        session.close()
        return client.clientid if client else None

    def save_new_equipment(self, equipment_data):
        session = self.get_session()
        try:
            new_equipment = Equipment(**equipment_data)
            session.add(new_equipment)
            session.commit()
            return True
        except Exception as e:
            print(f"exception {e}")
            session.rollback()
            return False